# AI Consensus Engine

AI Consensus Engine is a local-first Blanzy Labs AI app for comparing multiple LLM responses and producing a synthesized consensus.

Current release: `v0.1.1 - Blanzy Labs Standardization Patch`

Original MVP release: `v0.1.0 - Local Consensus MVP`

AI Consensus Engine is part of the Blanzy Labs AI app family.

## What It Does

- Runs a three-stage consensus workflow: primary answer, reviewer critique, and final synthesis.
- Lets users choose OpenAI or Gemini providers for each stage.
- Produces structured sections for agreement, disagreement, uncertainty, and follow-up questions.
- Exports the visible result as a local Markdown report in the browser.

## Current Scope

- Local-first FastAPI backend and React/Vite frontend.
- Bring-your-own provider API keys.
- OpenAI and Gemini provider support.
- Docker Compose support.
- No prompt history, result history, login, database, telemetry, analytics, or server-side result storage.

## Out Of Scope

- Hosted or production deployment.
- User accounts, authentication, teams, or share links.
- Database persistence or report history.
- Voice features.
- Hidden web browsing or research mode.
- Professional legal, financial, medical, security, or compliance advice.

## Roadmap

- v0.1.1: Blanzy Labs naming, docs, metadata, and release-readiness cleanup.
- v0.2.x: validation polish, docs normalization, and focused app improvements.
- Future provider or local-model expansion only where explicitly planned.

## Architecture

- Backend: FastAPI
- Frontend: React, Vite, TypeScript
- Providers: OpenAI and Gemini
- Runtime: local development or Docker Compose

See [docs/architecture.md](docs/architecture.md).

## Local Setup

```bash
git clone https://github.com/blanzy-labs/ai-consensus.git
cd ai-consensus
cp .env.example .env
```

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run test -- --run
npm run build
npm run dev
```

Open:

- Frontend: `http://localhost:5173`
- Backend health: `http://localhost:8000/health`

See [docs/local-install.md](docs/local-install.md).

## Docker Setup

```bash
cp .env.example .env
# edit .env with backend provider keys if needed
docker compose up --build
docker compose down
```

Docker Compose loads `.env` for the backend service. The frontend receives only non-secret configuration.

## Environment Variables

Root `.env` values:

```env
APP_NAME="AI Consensus Engine"
APP_ENV=development
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
FRONTEND_ORIGIN=http://localhost:5173

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini

GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.5-flash
```

Provider keys go only in the backend/root `.env`. Do not put OpenAI, Gemini, or other provider keys in frontend env files. `.env` is ignored by git; `.env.example` contains placeholders only and is safe to commit.

If a provider reports a model-not-found or unsupported-model error, update `OPENAI_MODEL` or `GEMINI_MODEL` in `.env`.

The frontend uses `VITE_API_BASE_URL` for the backend URL:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## Testing

Backend:

```bash
cd backend
pytest
```

Frontend:

```bash
cd frontend
npm run test -- --run
npm run build
```

Docker:

```bash
docker compose build
```

## Usage Workflow

1. Start the backend and frontend with Docker Compose or local development commands.
2. Add provider keys to the ignored `.env` file.
3. Open `http://localhost:5173`.
4. Enter a question.
5. Choose providers for the primary answer, reviewer, and synthesizer.
6. Run the consensus workflow.
7. Review the final answer, agreement, disagreement, uncertainty, and follow-up sections.
8. Export Markdown locally if needed.

## API Summary

- `GET /health`: returns backend status.
- `POST /consensus/run`: runs the consensus workflow.

The frontend calls only the local backend. Provider API keys remain backend-only.

## Troubleshooting

See [docs/troubleshooting.md](docs/troubleshooting.md).

## Security And Privacy

See [docs/security-and-privacy.md](docs/security-and-privacy.md).

Short version:

- API keys are backend-only.
- User prompts and generated responses are sent to configured providers.
- No prompt/result storage is implemented in V1.
- Markdown export is generated locally in the browser.
- Avoid submitting sensitive or private data unless you are comfortable sending it to the configured providers.

## Documentation

- [Architecture](docs/architecture.md)
- [Security and privacy](docs/security-and-privacy.md)
- [Security notes](docs/security.md)
- [Local install guide](docs/local-install.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Prompt design](docs/prompt-design.md)
- [Demo script](docs/demo-script.md)
- [Sample report](docs/sample-report.md)
- [Release checklist](docs/release-checklist.md)
- [Release notes](docs/release-notes/v0.1.1.md)
- [Validation notes](docs/validation/v0.1.1-validation.md)
- [Disclaimer](docs/disclaimer.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE](LICENSE).

## Disclaimer

See [docs/disclaimer.md](docs/disclaimer.md).
