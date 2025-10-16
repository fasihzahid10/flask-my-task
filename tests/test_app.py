import os
import pytest
from app import create_app, db
from app.models import User, Task

@pytest.fixture()
def client():
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    app = create_app()
    app.config.update(TESTING=True)
    with app.app_context():
        db.create_all()
        u = User(email="test@example.com"); u.set_password("password")
        db.session.add(u); db.session.commit()
    return app.test_client()

def login(client):
    # register test user
    client.post("/auth/register", data={"email": "t2@example.com", "password": "password"})
    # login
    client.post("/auth/login", data={"email": "t2@example.com", "password": "password"})

def test_homepage(client):
    r = client.get("/")
    assert r.status_code == 200

def test_task_crud(client):
    login(client)
    r = client.post("/task/create", data={"title": "Task A", "description": "X"})
    assert r.status_code in (302, 303)
    # toggle should work
    r = client.post("/task/1/toggle")
    assert r.status_code in (302, 303)
    # delete should work
    r = client.post("/task/1/delete")
    assert r.status_code in (302, 303)
