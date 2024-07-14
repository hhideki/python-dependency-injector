from typing import Tuple, Type

from di._constants import _DEFAULT_QUALIFIER
from di.container import Container
from di.injector import Injector

__version__ = "0.1.0"
__author__ = "Hugo Hideki Yamashita (hugo.hideki@gmail.com)"
__repo__ = "https://github.com/hhideki/python-dependency-injector"


injector = Injector()


def load_container(container: Container):
    global injector
    injector.load_container(container)


def load_containers(*containers: Tuple[Container, ...]):
    global injector
    injector.load_containers(*containers)


def inject(subject: Type, injector: Injector = injector, qualifier: str = _DEFAULT_QUALIFIER):
    return injector.inject(type=subject, qualifier=qualifier)
