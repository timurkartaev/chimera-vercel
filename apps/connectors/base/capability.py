from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, TypeVar
from typing import TypedDict, Required, NotRequired

Input = TypeVar("Input")
Output = TypeVar("Output")


class BaseCapabilityAction(ABC, Generic[Input, Output]):
    def __init__(self, description: str):
        self.description = description

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        raise AttributeError("Cannot set attribute")

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")

    def __call__(self, *args, **kwargs) -> Output:
        return self.execute(*args, **kwargs)

    def __set_name__(self, owner, name):
        self.name = name
        owner._actions[name] = self

    @abstractmethod
    def execute(self, *args, **kwargs) -> Output:
        pass


class BaseCapability(ABC):
    _actions: dict[str, BaseCapabilityAction] = {}

    def get_available_actions(self):
        return list(self._actions.keys())

    def get_action(self, name: str) -> BaseCapabilityAction:
        return self._actions[name]


# Authorize Capability


class AuthorizeBeginRequest(TypedDict):
    customer_id: str
    customer_name: str


class AuthorizeBeginResponse(TypedDict):
    auth_url: str
    auth_method: str
    auth_params: Dict[str, Any]


class AuthorizeFinalizeRequest(TypedDict):
    code: NotRequired[str]
    state: NotRequired[str]
    error: NotRequired[str]


class AuthorizeFinalizeResponse(TypedDict):
    status: str
    redirect_uri: Optional[str]


class BaseAuthorizeBeginCapabilityAction(
    BaseCapabilityAction[AuthorizeBeginRequest, AuthorizeBeginResponse]
):
    pass


class BaseAuthorizeFinalizeCapabilityAction(
    BaseCapabilityAction[AuthorizeFinalizeRequest, AuthorizeFinalizeResponse]
):
    pass


class BaseAuthorizeCapability(BaseCapability):
    begin: BaseAuthorizeBeginCapabilityAction
    finalize: BaseAuthorizeFinalizeCapabilityAction
