from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Generic, Optional, Type, TypeVar, Union, cast

from pydantic import BaseModel, ConfigDict, field_validator

TInput = TypeVar("TInput", bound=BaseModel)
TOutput = TypeVar("TOutput", bound=BaseModel)


class _RunnerWithParentContext(Generic[TInput, TOutput]):
    __slots__ = ("_context", "_fn", "_validator")

    def __init__(
        self,
        context: "BaseCapability",
        fn: Callable[[TInput, "BaseCapability"], TOutput],
        validator: Type[TInput],
    ):
        assert context, "Context must be an instance of BaseCapability"
        self._context = context
        self._fn = fn
        self._validator = validator

    def __call__(self, input_data: Union[Dict[str, Any], TInput]) -> Dict[str, Any]:
        validated = (
            self._validator(**input_data)
            if isinstance(input_data, dict)
            else input_data
        )
        output = self._fn(validated, self._context)
        return output.model_dump()


class BaseCapabilityAction(ABC, Generic[TInput, TOutput]):
    Input: Type[TInput]
    Output: Type[TOutput]

    def __init__(self, description: str):
        self.description = description

    def __get__(self, instance, owner):
        return _RunnerWithParentContext(instance, self.execute, self.Input)

    def __set__(self, instance, value):
        raise AttributeError("Cannot set attribute")

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")

    def __set_name__(self, owner, name):
        self.name = name
        owner._actions[name] = self

    @abstractmethod
    def execute(self, input_model: TInput, context: "BaseCapability") -> TOutput:
        pass


class BaseCapability(ABC):
    _actions: dict[str, BaseCapabilityAction] = {}

    def get_available_actions(self):
        return list(self._actions.keys())

    def get_action(self, name: str) -> BaseCapabilityAction:
        return self._actions[name]


# Authorize Capability


class AuthorizeBeginCapabilityAction(BaseCapabilityAction):
    class Input(BaseModel):
        customer_id: str
        customer_name: str

    class Output(BaseModel):
        auth_url: str
        auth_method: str
        auth_params: list[dict[str, Any]]


class AuthorizeFinalizeCapabilityAction(BaseCapabilityAction):
    class Input(BaseModel):
        code: Optional[str] = None
        state: Optional[str] = None
        error: Optional[str] = None
        extras: Dict[str, Any] = {}

        model_config = ConfigDict(extra="allow")

        @field_validator("extras", mode="before")
        @classmethod
        def extract_extras(cls, v, info):
            # info.data is available in Pydantic v2 for validators in `mode="before"`
            # Get all fields from the input data
            data = info.data or {}
            known_keys = {"code", "state", "error", "extras"}
            return {k: v for k, v in data.items() if k not in known_keys}

    class Output(BaseModel):
        status: str
        redirect_uri: Optional[str] = None
        error_message: Optional[str] = None


class BaseAuthorizeCapability(BaseCapability):
    begin: AuthorizeBeginCapabilityAction
    finalize: AuthorizeFinalizeCapabilityAction
