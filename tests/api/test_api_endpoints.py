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
    get_url = "http://localhost:8000"
    post_url = "http://localhost:8000/add-product"

    payload = {
        "category": "Drinks",
        "product": "Coffee",
        "price": 3.99
    }

    s.post(post_url, json=payload)
    response = s.get(get_url)
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["data"][0]["category"] == "electronics"
    assert data["data"][0]["product"] == "smartphone"
    assert data["data"][0]["price"] == 699.99
    assert data["data"][1]["category"] == "drinks"
    assert data["data"][1]["product"] == "coffee"
    assert data["data"][1]["price"] == 3.99
    
def test_calculate_sums_by_category():
    s = requests.Session()

    payload = {
        "category": "Drinks",
        "product": "Tea",
        "price": 2.99
    }
    s.post("http://localhost:8000/add-product", json=payload)

    sum_url = "http://localhost:8000/sums-by-category"
    
    response = s.get(sum_url)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["data"][0]["total_price"] == 6.98
    assert data["data"][1]["total_price"] == 699.99


def test_delete_product():
    s = requests.Session()
    response_id = s.get("http://localhost:8000").json()["data"][0]["id"]
    delete_url = f"http://localhost:8000/delete-product/{response_id}"
    response = s.delete(delete_url)

    assert response.status_code == 200
    assert len(s.get("http://localhost:8000").json()["data"]) == 2
