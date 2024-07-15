# Provider

Providers are classes that will provide a dependency.

Currently there are 2 provider flavors: `Factory` and `Singleton`.


# Intefaces

## Provider

This interface that uses `Generic` and defines two methods that needs to be implemented: `__init__` and `provide`.

### __init__(self, block: Callable[, qualifier: str])

This method initializes the provider, configuring how data will be injected.

The `block` is a `Callable` that receives no parameters and returns the dependency.

The `qualifier` is optional. It defines an identifier for the injector, usually used in cases where multiple providers for the same type of data must be defined.

### provide(self, *args, **kwargs)

This method provides the dependency.

The only mandatory implementation is the return of the dependency.


# Classes

## Factory

This class defines a factory provider, which will always invoke the provider block.

**Implements:** `Provider`

### __init__(self, block: Callable[, qualifier: str])

Initializes the provider object.

The `block` is a `Callable` that receives no parameters and returns the dependency.

The `qualifier` is optional. It defines an identifier for the injector, usually used in cases where multiple providers for the same type of data must be defined.


### provide(self, *args, **kwargs)

This method provides the dependency. Every time this method is called, the `block` provided in the `__init__` method will be invoked.

**Returns:** Value returned by the `Callable` set in the initializer.


## Singleton

This class defines a singleton provider, which will cache data to prevent invoking the provider block in each call.

**Implements:** `Provider`

### __init__(self, block: Callable[, qualifier: str])

Initializes the provider object.

The `block` is a `Callable` that receives no parameters and returns the dependency.

The `qualifier` is optional. It defines an identifier for the injector, usually used in cases where multiple providers for the same type of data must be defined.


### provide(self, *args, **kwargs)

This method provides the dependency. Once this method is called, the valur returned by the `block` provided in the `__init__` will be cached. Future calls to this method will return the cached data.

**Returns:** The value returned by the `Callable` set in the initializer. Once the `Callable` is invoked, returns the cached value.
