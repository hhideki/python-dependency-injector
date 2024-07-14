import pytest

from di.container import Container
from di.error import ProviderNotFoundError
from di.injector import Injector
from di.provider import Factory, Singleton


class TestInjector:
    def test_create_empty_injector(self):
        injector = Injector()

        assert len(injector.providers) == 0


    def test_create_injector_with_empty_container(self):
        container = Container()
        injector = Injector()

        injector.load_container(container)

        assert len(injector.providers) == 0


    def test_attempt_to_inject_with_empty_injector(self):
        with pytest.raises(ProviderNotFoundError):
            injector = Injector()
            injector.inject(int)


    def test_attempt_to_inject_without_provider(self):
        with pytest.raises(ProviderNotFoundError):
            container = Container(
                Factory[int](lambda: 42)
            )
            injector = Injector()
            injector.load_container(container)
            injector.inject(str)


    def test_inject_correct_value_without_qualifier(self):
        container = Container(
            Factory[int](lambda: 42),
            Factory[str](lambda: "teste")
        )

        injector = Injector()
        injector.load_container(container)

        int_value = injector.inject(int)
        str_value = injector.inject(str)

        assert int_value == 42
        assert str_value == "teste"


    def test_inject_correct_value_with_qualifier(self):
        container = Container(
            Factory[int](lambda: 1, "FIRST PROVIDER"),
            Factory[int](lambda: 2, "SECOND PROVIDER")
        )

        injector = Injector()
        injector.load_container(container)

        first_value = injector.inject(int, "FIRST PROVIDER")
        second_value = injector.inject(int, "SECOND PROVIDER")

        assert first_value == 1
        assert second_value == 2


    def test_inject_correct_value_with_override(self):
        container = Container(
            Factory[int](lambda: 1),
            Factory[int](lambda: 2)
        )

        injector = Injector()
        injector.load_container(container)

        value = injector.inject(int)

        assert value == 2
