# Container

A `Container` is a class that groups `Provider`s.


### \_\_init\_\_(self, *args)

Initializes the `Container` object.

The `*args` parameter is a list of `Provider`s.

**Throws:**
- `NotAProviderError`: If any of the values is `*args` is not a `Provider`.
