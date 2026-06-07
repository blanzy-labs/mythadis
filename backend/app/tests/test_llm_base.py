import pytest

from app.llm.base import BaseLLMProvider


def test_base_provider_contract_exists() -> None:
    assert hasattr(BaseLLMProvider, "generate")


def test_base_provider_requires_generate() -> None:
    with pytest.raises(TypeError):
        BaseLLMProvider()


def test_provider_interface_exposes_generate() -> None:
    class TestProvider(BaseLLMProvider):
        def generate(self, prompt: str) -> str:
            return prompt

    provider = TestProvider()

    assert provider.generate("Hello") == "Hello"
