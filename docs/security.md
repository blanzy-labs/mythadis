# Security

API keys will be backend-only. The frontend must not receive OpenAI, Gemini, or other provider secrets.

`.env` files must not be committed. Use `.env.example` for placeholder configuration only.

No prompt storage is planned in V1. No login or authentication is planned in V1. Users will bring their own API keys when provider support is added.
