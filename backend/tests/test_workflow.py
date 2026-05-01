from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def token():
    r=client.post('/auth/login',data={'username':'admin@example.com','password':'password123'})
    return r.json()['access_token']

def test_onboarding():
    t=token()
    r=client.post('/lifecycle/onboarding',json={'employee_id':1},headers={'Authorization':f'Bearer {t}'})
    assert r.status_code==200
