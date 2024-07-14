import pytest

from di.container import Container
from di.error import NotAProviderError
from di.provider import Factory, Singleton

class TestContainer:
    def test_create_empty_container(self):
        container = Container()

        assert container is not None
        assert len(container.providers) == 0


    def test_create_container_without_Provider(self):
        with pytest.raises(NotAProviderError):
            container = Container("some string")


    def test_create_container_with_single_provider(self):
        container = Container(
            Factory[int](lambda: 42)
        )

        assert len(container.providers) == 1


    def test_create_container_with_multiple_providers(self):
        container = Container(
            Factory[int](lambda: 42),
            Singleton[str](lambda: "Test string")
        )

        assert len(container.providers) == 2


    def test_create_container_with_providers_override(self):
        first_provider = Factory[int](lambda: 42)
        second_provider = Factory[int](lambda: 99)
        container = Container(
            first_provider,
            second_provider
        )

        assert len(container.providers) == 1
        assert list(container.providers.values())[0] == second_provider


    def test_create_container_with_providers_with_qualifiers(self):
        container = Container(
            Factory[int](lambda: 1, "FIRST PROVIDER"),
            Factory[int](lambda: 2, "SECOND PROVIDER"),
            Singleton[int](lambda: 3, "THIRD PROVIDER"),
            Factory[int](lambda: 4),
            Factory[int](lambda: 5),
            Singleton[int](lambda: 6, "THIRD PROVIDER")
        )

        assert len(container.providers) == 4
