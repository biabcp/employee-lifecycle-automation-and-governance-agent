from fastapi.testclient import TestClient
from app.main import app
from app.seed import run

run()
client=TestClient(app)

def test_login():
    r=client.post('/auth/login',data={'username':'admin@example.com','password':'password123'})
    assert r.status_code==200
    assert 'access_token' in r.json()
