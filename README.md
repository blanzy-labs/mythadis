# Mythadis Consensus Engine

Mythadis Consensus Engine is an open-source companion project from Mythadis Labs. It will explore a simple consensus pattern where one AI answers a question, another AI reviews that answer, and a final synthesis is produced from agreement, disagreement, and uncertainty.

Current status: foundation build only. This slice creates the project structure, backend health check, frontend shell, environment handling, Docker setup, and starter documentation.

This app does not call OpenAI or Gemini yet.

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

Verify the backend:

```bash
curl http://localhost:8000/health
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## Docker Setup

From the repository root:

```bash
docker compose up --build
```

The backend runs at `http://localhost:8000` and the frontend runs at `http://localhost:5173`.

## Environment Variables

Copy `.env.example` to `.env` for local development and update values as needed.

API key values are included as placeholders only. Empty keys are allowed in this foundation slice.

## Security and Privacy

Do not commit `.env` files or real API keys. Future LLM provider keys should remain backend-only and should never be exposed to the frontend.

No login, database, prompt storage, or LLM calls are implemented in this slice.
