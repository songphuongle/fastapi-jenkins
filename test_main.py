from fastapi.testclient import TestClient
from main import app

# test comment
client = TestClient(app)

def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_2():
    response = client.get("/check_prime?number=2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_3():
    response = client.get("/check_prime?number=3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_4():
    response = client.get("/check_prime?number=4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_10():
    response = client.get("/check_prime?number=10")
    assert response.status_code == 200
    assert response.json() == {"number": 10, "is_prime": False}

def test_check_prime_negative():
    response = client.get("/check_prime?number=-1")
    assert response.status_code == 200
    assert response.json() == {"number": -1, "is_prime": False}

def test_check_prime_zero():
    response = client.get("/check_prime?number=0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_large_prime():
    response = client.get("/check_prime?number=97")
    assert response.status_code == 200
    assert response.json() == {"number": 97, "is_prime": True}

def test_check_prime_large_non_prime():
    response = client.get("/check_prime?number=100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

def test_check_prime_float():
    response = client.get("/check_prime?number=10.5")
    assert response.status_code == 422
