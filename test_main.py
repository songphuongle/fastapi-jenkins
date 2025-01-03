from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")
    print(f"Test GET /get_version: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_2():
    response = client.get("/check_prime/2")
    print(f"Test /check_prime/2: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_3():
    response = client.get("/check_prime/3")
    print(f"Test /check_prime/3: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_4():
    response = client.get("/check_prime/4")
    print(f"Test /check_prime/4: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_10():
    response = client.get("/check_prime/10")
    print(f"Test /check_prime/10: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 10, "is_prime": False}

def test_check_prime_negative():
    response = client.get("/check_prime/-1")
    print(f"Test /check_prime/-1: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": -1, "is_prime": False}

def test_check_prime_zero():
    response = client.get("/check_prime/0")
    print(f"Test /check_prime/0: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_large_prime():
    response = client.get("/check_prime/97")
    print(f"Test /check_prime/97: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 97, "is_prime": True}

def test_check_prime_large_non_prime():
    response = client.get("/check_prime/100")
    print(f"Test /check_prime/100: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

def test_check_prime_float():
    response = client.get("/check_prime/10.5")
    print(f"Test /check_prime/10.5: Status Code: {response.status_code}, Response: {response.json() if response.status_code != 422 else 'Unprocessable Entity'}")
    assert response.status_code == 422
