from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Optional,
    Type,
    TypeVar,
    Union,
)

from pydantic import BaseModel
from apps.connectors.base.utils import get_integration_configs
from apps.connectors.base.loader import load_integration_overrides
from apps.connectors.base.models import ConnectorConfig


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
        self._overrides: Dict[str, "BaseCapabilityAction"] = {}
        print("description", description)

    def override_action(self, integration_key: str, action: "BaseCapabilityAction"):
        self._overrides[integration_key] = action

    def __get__(self, instance, owner):
        slug = instance.config.info.slug if instance and instance.config else None
        action = self._overrides.get(slug, self)
        return _RunnerWithParentContext(instance, action.execute, self.Input)

    def __set__(self, instance, value):
        raise AttributeError("Cannot set attribute")

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")

    def __set_name__(self, owner, name):
        self.name = name
        if not hasattr(owner, "_actions"):
            owner._actions = {}
        owner._actions[name] = self

    @abstractmethod
    def execute(self, input_model: TInput, context: "BaseCapability") -> TOutput:
        pass


class BaseCapability(ABC):
    _actions: Dict[str, BaseCapabilityAction] = {}

    def __init__(self, config: Optional["ConnectorConfig"] = None):
        self.config = config
        self._load_integration_overrides()

    def get_available_actions(self):
        return list(self._actions.keys())

    def get_action(self, name: str) -> BaseCapabilityAction:
        return self._actions[name]

    def _load_integration_overrides(self):
        if not self.config:
            return

        integration_key = self.config.info.slug
        capability_key = self.__class__.__name__.lower().replace("capability", "")
        overrides_module = load_integration_overrides(integration_key)

        if not overrides_module:
            return

        for name in dir(overrides_module):
            if not name.startswith(f"{capability_key}__"):
                continue

            action_instance = getattr(overrides_module, name)
            if not isinstance(action_instance, BaseCapabilityAction):
                continue
            try:
                _, action_name = name.split("__", 1)
                capability_action = self._actions[action_name]
                capability_action.override_action(integration_key, action_instance)
            except KeyError:
                raise ValueError(
                    f"No action '{action_name}' defined on capability '{self.__class__.__name__}' "
                    f"to override with '{name}' in integration '{integration_key}'"
                )
