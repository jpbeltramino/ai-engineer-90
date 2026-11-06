# AI Engineer 90

A small FastAPI service built as part of a 90-day plan to move from backend
development into AI engineering. Week 1 sets up the foundation: a typed API,
tests, a container image and CI. In week 2 the echo endpoint is replaced by a
real LLM call.

## Endpoints

| Method | Path          | Description                              |
| ------ | ------------- | ---------------------------------------- |
| GET    | `/health`     | Liveness check                           |
| POST   | `/chat/echo`  | Echoes the last user message (placeholder) |

Interactive docs are available at `http://localhost:8000/docs` when the server is running.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## Test and lint

```bash
pytest
ruff check .
```

## Run with Docker

```bash
docker build -t ai-engineer-90 .
docker run --rm -p 8000:8000 ai-engineer-90
curl http://localhost:8000/health
```

## Example request

```bash
curl -X POST http://localhost:8000/chat/echo \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

## Project layout

```
app/
  main.py      FastAPI application and routes
  models.py    Pydantic request and response models
tests/
  test_main.py
Dockerfile
.github/workflows/ci.yml
```

## Roadmap

- [x] Week 1: typed API, tests, Docker, CI
- [ ] Week 2: LLM API integration, streaming, token and cost tracking
- [ ] Week 3: structured output and tool calling
- [ ] Week 4: first complete chatbot with a simple UI
