from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_echo_returns_last_user_message() -> None:
    payload = {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi!"},
            {"role": "user", "content": "How are you?"},
        ]
    }
    response = client.post("/chat/echo", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["reply"]["role"] == "assistant"
    assert body["reply"]["content"] == "You said: How are you?"
    assert body["estimated_tokens"] >= 1


def test_chat_echo_rejects_empty_messages() -> None:
    response = client.post("/chat/echo", json={"messages": []})
    assert response.status_code == 422


def test_chat_echo_rejects_invalid_role() -> None:
    response = client.post(
        "/chat/echo", json={"messages": [{"role": "robot", "content": "Hi"}]}
    )
    assert response.status_code == 422


def test_chat_echo_requires_a_user_message() -> None:
    response = client.post(
        "/chat/echo", json={"messages": [{"role": "system", "content": "Be nice"}]}
    )
    assert response.status_code == 422
