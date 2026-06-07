import types

import pytest

from app.config import Settings
from app.llm.base import MissingProviderConfigError, ProviderRequestError
from app.llm.openai_client import OpenAIProvider


def test_openai_provider_fails_clearly_when_api_key_missing() -> None:
    settings = Settings(_env_file=None, openai_api_key="")
    provider = OpenAIProvider(settings)

    with pytest.raises(MissingProviderConfigError) as exc_info:
        provider.generate("Hello")

    message = str(exc_info.value)
    assert message == "OpenAI API key is not configured. Set OPENAI_API_KEY in your .env file."
    assert "secret-key" not in message


def test_openai_provider_uses_configured_model_and_returns_text(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = {}

    class FakeResponses:
        def create(self, model: str, input: str) -> types.SimpleNamespace:
            calls["model"] = model
            calls["input"] = input
            return types.SimpleNamespace(output_text="OpenAI answer")

    class FakeOpenAI:
        def __init__(self, api_key: str) -> None:
            calls["api_key"] = api_key
            self.responses = FakeResponses()

    monkeypatch.setitem(__import__("sys").modules, "openai", types.SimpleNamespace(OpenAI=FakeOpenAI))
    settings = Settings(_env_file=None, openai_api_key="secret-key", openai_model="gpt-test")
    provider = OpenAIProvider(settings)

    response = provider.generate("Hello")

    assert response == "OpenAI answer"
    assert calls == {"api_key": "secret-key", "model": "gpt-test", "input": "Hello"}


def test_openai_provider_wraps_provider_failures(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeResponses:
        def create(self, model: str, input: str) -> types.SimpleNamespace:
            raise RuntimeError("secret-key leaked by SDK")

    class FakeOpenAI:
        def __init__(self, api_key: str) -> None:
            self.responses = FakeResponses()

    monkeypatch.setitem(__import__("sys").modules, "openai", types.SimpleNamespace(OpenAI=FakeOpenAI))
    settings = Settings(_env_file=None, openai_api_key="secret-key")
    provider = OpenAIProvider(settings)

    with pytest.raises(ProviderRequestError) as exc_info:
        provider.generate("Hello")

    message = str(exc_info.value)
    assert message == "OpenAI request failed. Check your API key, model name, and network connection."
    assert "secret-key" not in message
