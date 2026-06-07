import sys
import types

import pytest

from app.config import Settings
from app.llm.base import MissingProviderConfigError, ProviderRequestError
from app.llm.gemini_client import GeminiProvider


def test_gemini_provider_fails_clearly_when_api_key_missing() -> None:
    settings = Settings(_env_file=None, gemini_api_key="")
    provider = GeminiProvider(settings)

    with pytest.raises(MissingProviderConfigError) as exc_info:
        provider.generate("Hello")

    message = str(exc_info.value)
    assert message == "Gemini API key is not configured. Set GEMINI_API_KEY in your .env file."
    assert "secret-key" not in message


def test_gemini_provider_uses_configured_model_and_returns_text(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = {}

    class FakeGenerativeModel:
        def __init__(self, model_name: str) -> None:
            calls["model"] = model_name

        def generate_content(self, prompt: str) -> types.SimpleNamespace:
            calls["prompt"] = prompt
            return types.SimpleNamespace(text="Gemini answer")

    fake_genai = types.ModuleType("google.generativeai")
    fake_genai.configure = lambda api_key: calls.update({"api_key": api_key})
    fake_genai.GenerativeModel = FakeGenerativeModel
    fake_google = types.ModuleType("google")
    fake_google.generativeai = fake_genai

    monkeypatch.setitem(sys.modules, "google", fake_google)
    monkeypatch.setitem(sys.modules, "google.generativeai", fake_genai)
    settings = Settings(_env_file=None, gemini_api_key="secret-key", gemini_model="gemini-test")
    provider = GeminiProvider(settings)

    response = provider.generate("Hello")

    assert response == "Gemini answer"
    assert calls == {"api_key": "secret-key", "model": "gemini-test", "prompt": "Hello"}


def test_gemini_provider_wraps_provider_failures(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeGenerativeModel:
        def __init__(self, model_name: str) -> None:
            pass

        def generate_content(self, prompt: str) -> types.SimpleNamespace:
            raise RuntimeError("secret-key leaked by SDK")

    fake_genai = types.ModuleType("google.generativeai")
    fake_genai.configure = lambda api_key: None
    fake_genai.GenerativeModel = FakeGenerativeModel
    fake_google = types.ModuleType("google")
    fake_google.generativeai = fake_genai

    monkeypatch.setitem(sys.modules, "google", fake_google)
    monkeypatch.setitem(sys.modules, "google.generativeai", fake_genai)
    settings = Settings(_env_file=None, gemini_api_key="secret-key")
    provider = GeminiProvider(settings)

    with pytest.raises(ProviderRequestError) as exc_info:
        provider.generate("Hello")

    message = str(exc_info.value)
    assert message == "Gemini request failed. Check your API key, model name, and network connection."
    assert "secret-key" not in message
