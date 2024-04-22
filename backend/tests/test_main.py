from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_deposit():
    response = client.post(
        "/deposit",
        json={"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6},
    )
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10050.00,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75,
        "30.04.2021": 10201.51,
        "31.05.2021": 10252.51,
        "30.06.2021": 10303.78,
        "31.07.2021": 10355.29,
    }


def test_deposit_invalid_date():
    response = client.post(
        "/deposit", json={"date": "01.01", "periods": 3, "amount": 1000, "rate": 5}
    )
    assert response.status_code == 422


def test_deposit_invalid_periods():
    response = client.post(
        "/deposit", json={"date": "01.01.2022", "periods": 0, "amount": 1000, "rate": 5}
    )
    assert response.status_code == 422


def test_deposit_invalid_amount():
    response = client.post(
        "/deposit", json={"date": "01.01.2022", "periods": 3, "amount": 0, "rate": 5}
    )
    assert response.status_code == 422


def test_deposit_invalid_rate():
    response = client.post(
        "/deposit", json={"date": "01.01.2022", "periods": 3, "amount": 1000, "rate": 0}
    )
    assert response.status_code == 422
