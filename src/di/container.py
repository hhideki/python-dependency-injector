from typing import Any, Dict, Tuple, get_args

from di.error import NotAProviderError
from di.provider import Provider


class Container:
    providers: Dict[Tuple[Any, str], Provider] = None


    def __init__(self, *args: Tuple[Provider, ...]):
        if all(isinstance(arg, Provider) for arg in args) == False:
            raise NotAProviderError("Only Providers are accepted")

        self.providers = {}

        for arg in args:
            self.providers[(get_args(arg.__orig_class__)[0], arg.qualifier)] = arg
