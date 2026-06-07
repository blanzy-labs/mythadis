from app.config import Settings
from app.llm.base import BaseLLMProvider, UnsupportedProviderError
from app.llm.gemini_client import GeminiProvider
from app.llm.openai_client import OpenAIProvider


def get_provider(provider_name: str, settings: Settings) -> BaseLLMProvider:
    provider = provider_name.lower().strip()

    if provider == "openai":
        return OpenAIProvider(settings)

    if provider == "gemini":
        return GeminiProvider(settings)

    raise UnsupportedProviderError(f"Unsupported provider: {provider_name}")
