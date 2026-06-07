import pytest

from app.config import Settings
from app.llm.base import UnsupportedProviderError
from app.llm.gemini_client import GeminiProvider
from app.llm.openai_client import OpenAIProvider
from app.llm.provider_factory import get_provider


def test_get_provider_returns_openai_provider() -> None:
    settings = Settings(_env_file=None)

    provider = get_provider("openai", settings)

    assert isinstance(provider, OpenAIProvider)


def test_get_provider_returns_gemini_provider() -> None:
    settings = Settings(_env_file=None)

    provider = get_provider("gemini", settings)

    assert isinstance(provider, GeminiProvider)


def test_get_provider_rejects_unsupported_provider() -> None:
    settings = Settings(_env_file=None)

    with pytest.raises(UnsupportedProviderError, match="Unsupported provider: xyz"):
        get_provider("xyz", settings)
