# Injector

An `Injector` is a class that aggregate `Provider`s to inject dependencies.


### load_container(self, container: Container)

Loads a `Container`, aggregating its `Provider`s.


### load_containers(self, *containers: tuple[Container, ...])

Loads `Container`s, aggregating their `Provider`s.


### inject(self, type: Type, [qualifier: str])

Injects a dependency of a type passed in `type`.

If a `qualifier` is provided, searches for a `Provider` with the same `type` and `qualifier`.

**Throws:**
- `ProviderNotFoundError`: if a `Provider` is not found for the given `type` and `qualifier`.

**Returns:** Dependency found by a `Provider`.
