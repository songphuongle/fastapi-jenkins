from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")  # Correct path
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_2():
    response = client.get("/check_prime/2")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_3():
    response = client.get("/check_prime/3")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_4():
    response = client.get("/check_prime/4")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_10():
    response = client.get("/check_prime/10")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 10, "is_prime": False}

def test_check_prime_negative():
    response = client.get("/check_prime/-1")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": -1, "is_prime": False}

def test_check_prime_zero():
    response = client.get("/check_prime/0")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_large_prime():
    response = client.get("/check_prime/97")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 97, "is_prime": True}

def test_check_prime_large_non_prime():
    response = client.get("/check_prime/100")  # Correct path parameter
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

def test_check_prime_float():
    response = client.get("/check_prime/10.5")  # This will give a 422 as expected
    assert response.status_code == 422
