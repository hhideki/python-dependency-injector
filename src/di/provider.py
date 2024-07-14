from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar, override

from di._constants import _DEFAULT_QUALIFIER


T_DEPENDENCY = TypeVar("T_DEPENDENCY")

class Provider(ABC, Generic[T_DEPENDENCY]):
    @abstractmethod
    def __init__(self, block: Callable[[], T_DEPENDENCY], qualifier: str = _DEFAULT_QUALIFIER):
        pass


    @abstractmethod
    def provide(self, *args, **kwargs) -> T_DEPENDENCY:
        pass


class Factory(Provider[T_DEPENDENCY]):
    callable: Callable[[], T_DEPENDENCY] = None
    qualifier: str = None


    @override
    def __init__(self, block: Callable[[], T_DEPENDENCY], qualifier: str = _DEFAULT_QUALIFIER):
        self.callable = block
        self.qualifier = qualifier


    @override
    def provide(self) -> T_DEPENDENCY:
        return self.callable()


class Singleton(Provider[T_DEPENDENCY]):
    callable: Callable[[], T_DEPENDENCY] = None
    qualifier: str = None
    value: T_DEPENDENCY = None


    @override
    def __init__(self, block: Callable[[], T_DEPENDENCY], qualifier: str = _DEFAULT_QUALIFIER):
        self.callable = block
        self.qualifier: str = qualifier


    @override
    def provide(self) -> T_DEPENDENCY:
        if self.value is None:
            self.value = self.callable()
            self.callable = None

        return self.value
