from typing import Any, Dict, Type

from di._constants import _DEFAULT_QUALIFIER
from di.container import Container
from di.error import ProviderNotFoundError
from di.provider import Provider

class Injector:
    providers: Dict[Any, Provider] = None


    def __init__(self):
        self.providers = {}


    def load_container(self, container: Container):
        self.providers.update(container.providers.copy())


    def load_containers(self, *containers: tuple[Container, ...]):
        for c in containers:
            self.load_container(c)


    def inject(self, type: Type, qualifier: str = _DEFAULT_QUALIFIER):
        key = (type, qualifier)

        if key not in self.providers:
            raise ProviderNotFoundError(f"Could not find suitable provider: [{key}]")

        return self.providers[key].provide()
