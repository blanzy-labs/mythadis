# Architecture

## Purpose

Mythadis Consensus Engine will help compare and synthesize AI responses. The planned product flow is:

1. User asks a question.
2. A primary model produces an answer.
3. A reviewer model critiques the answer.
4. A final synthesis identifies agreement, disagreement, and uncertainty.

## Current Foundation

This slice includes a FastAPI backend, a React/Vite frontend, shared environment configuration, Docker Compose, and starter documentation.

The backend currently exposes only `/health`. The frontend displays the project title, tagline, backend health status, and a placeholder for the future workflow.

No LLM providers, authentication, database, prompt history, or mock AI responses are implemented yet.
