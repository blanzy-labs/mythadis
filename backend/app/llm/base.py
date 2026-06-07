from abc import ABC, abstractmethod


class ProviderError(Exception):
    """Base class for safe, user-facing provider errors."""


class MissingProviderConfigError(ProviderError):
    """Raised when a provider is missing required configuration."""


class ProviderRequestError(ProviderError):
    """Raised when a provider request fails."""


class UnsupportedProviderError(ProviderError):
    """Raised when a requested provider is not supported."""


class BaseLLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a text response for the supplied prompt."""
