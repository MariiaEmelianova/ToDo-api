from fastapi.testclient import TestClient
from app_final import app, MAX_TASKS

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()

def test_create_task():
    response = client.post("/tasks", json={"title": "Buy bread"})
    assert response.status_code == 200
    assert response.json()["title"] == "Buy bread"

def test_get_task_by_id():
    client.post("/tasks", json={"title": "Test task"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_limit_error():
    for i in range(15):
        client.post("/tasks", json={"title": f"Task {i}"})
    response = client.post("/tasks", json={"title": "Extra"})
    assert response.status_code == 400
