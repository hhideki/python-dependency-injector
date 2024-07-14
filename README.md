# python-dependency-injector
Simple python dependency injector library.

**Latest version:** `0.1.0`

The changelog can be found [here](docs/changelog).


## How to use
There are 3 steps to use this library:
1. Create a `Container`.
2. Load the `Container`.
3. Inject a dependency.


## Examples
### Simple injection
When a `Factory` provider is created, every time the provider's `inject` method is called, the `Callable` will be called.
```python
from di.container import Container
from di.provider import Factory
from di.injector import Injector

container = Container(
    Factory[int](lambda: 42), # Injects the number 42
    Factory[str](lambda: "A text") # Injects a string
)

injector = Injector()
injector.load_container(container)

my_number = injector.inject(int) # my_number == 42
my_text = injector.inject(str) # my_text == "A text"
```


### Singleton injection
When a `Singleton` provider is created, the `Callable` passed will only be called once and the result value will be cached.
```python
from random import randint

from di.container import Container
from di.provider import Singleton
from di.injector import Injector

container = Container(
    Singleton[int](lambda: randint())
)

injector = Injector()
injector.load_container(container)

my_number = injector.inject(int) # Suppose the injected value is 42
my_number2 = injector_inject(int) # Will inject the same number
```


## Providers with qualifiers
A qualifier is anything that can identify a `Provider`.
```python
from di.container import Container
from di.provider import Fatory
from di.injector import Injector

container = Container(
    Factory[int](lambda: 1, "INITIAL VALUE"),
    Factory[int](lambda: 42, "ANSWER TO EVERYTHING")
)

injector = Injector()
injector.load_container(container)

first_value = injector.inject("INITIAL VALUE") # first_value == 1
second_value = injector.inject("ANSWER TO EVERYTHING") # second_value == 42
```


## Overriding providers
When multiple `Provider`s are created for the same data type, the last `Provider` to be loaded will override all other `Provider`s.
```python
from di.container import Container
from di.provider import Fatory
from di.injector import Injector

container_1 = Container(
    Factory[int](lambda: 1)
)

container_2 = Container(
    Factory[int](lambda: 99)
)

injector = Injector()
injector.load_containers(container_1, container_2)

int_value = injector.inject(int) # int_value == 99
```


## Dependency with dependencies
You can inject dependencies in the `Provider`s definitions.
```python
from di.container import Container
from di.provider import Fatory
from di.injector import Injector

class MyDataClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

injector = Injector()

container = Container(
    Factory[int](lambda: 1),
    Factory[str](lambda: "John Doe"),
    Factory[MyDataClass](lambda: MyDataClass(name=injector.inject(str), age=injector.inject(int)))
)

injector.load_container(container)

my_obj = injector.inject(MyDataClass)
# my_obj.name == "John Doe"
# my_obj.age == 1
```
