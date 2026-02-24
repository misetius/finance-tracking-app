import pytest
import requests

def test_get_all_products_without_data():
    s = requests.Session()
    url = "http://localhost:8000"
    response = s.get(url)
    assert response.status_code == 200


def test_add_product():
    s = requests.Session()
    url = "http://localhost:8000/add-product"
    payload = {
        "category": "Electronics",
        "product": "Smartphone",
        "price": 699.99
    }
    response = s.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == f"Product added successfully"

def test_get_all_products():
    s = requests.Session()
    url = "http://localhost:8000"
    response = s.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data[0]["category"] == "Electronics"
    assert data[0]["product"] == "Smartphone"
    assert data[0]["price"] == 699.99
    




