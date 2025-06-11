from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Type,
    TypeVar,
    Union,
)

from pydantic import (
    BaseModel,
)


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
