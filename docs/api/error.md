# Errors

Some error classes are defined.
- `NotAContainerError`
- `NotAProviderError`
- `ProviderNotFoundError`

These errors only exist to give more meaning to an error that may occur.


## Classes

### NotAContainerError

Represents an error when a `Container` is expected but something else is found.


### NotAProviderError

Represents an error when a `Provider` is expected but something else is found.


### ProviderNotFoundError

Represents an error when an injection os requested for a type that has no `Provider` loaded.
