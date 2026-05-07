import pytest
import time
from analysis.tests.product_functions import add_product

def test_sums_by_category_with_one_product(client):

    # Add a product
    add_product(category='food', product='pizza', price=10.0)
    
    # Get sums by category for the current year
    response = client.get('/sums-by-category?year=2026')
    print(response.json)
    assert response.status_code == 200
    data = response.json['data']
    assert len(data) == 1
    assert data[0]['category'] == 'food'
    assert data[0]['total_price'] == 10.0

def test_sums_by_category_with_multiple_products(client):

    # Add multiple products
    add_product(category='food', product='burger', price=5.0)
    add_product(category='food', product='pasta', price=7.0)
    add_product(category='drinks', product='soda', price=2.0)
    add_product(category='drinks', product='juice', price=3.0)
    
    # Get sums by category for the current year
    response = client.get('/sums-by-category?year=2026')
    print(response.json)
    assert response.status_code == 200
    data = response.json['data']
    assert len(data) == 2
    assert any(item['category'] == 'food' and item['total_price'] == 12.0 for item in data)
    assert any(item['category'] == 'drinks' and item['total_price'] == 5.0 for item in data)