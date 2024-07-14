from time import time_ns

from di.provider import Factory, Singleton

class TestProvider:
    def test_factory_provider_always_create_new_objects(self):
        provider = Factory[int](lambda: time_ns())

        first_value = provider.provide()
        second_value = provider.provide()

        assert first_value != second_value


    def test_singleton_provider_invokes_callable_only_once(self):
        provider = Singleton[int](lambda: str(time_ns()))

        first_value = provider.provide()
        second_value = provider.provide()

        assert first_value is second_value
        assert first_value == second_value
        assert id(first_value) == id(second_value)

