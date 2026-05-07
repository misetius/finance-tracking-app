import pytest
import time

def test_get_values_from_empty_database(client):
    response = client.get('/api/get-all')
    assert response.status_code == 200
    assert response.json == {'data': []}

def test_add_and_get_value(client):
    # Add a new value
    response = client.post('/api/add-product', json={
        'price': 2.0,
        'category': 'food',
        'product': 'bread'
    })
    assert response.status_code == 201
    
    # Get all values and check if the new value is present
    response = client.get('/api/get-all')
    assert response.status_code == 200
    data = response.json['data']
    assert len(data) == 1
    assert data[0]['price'] == 2.0
    assert data[0]['category'] == 'food'
    assert data[0]['product'] == 'bread'


def test_delete_item(client):
    # Add a new value to delete
    response = client.post('/api/add-product', json={
        'price': 50.0,
        'category': 'Entertainment',
        'product': 'Movie tickets'
    })
   

    response = client.get('/api/get-all')
    
    assert response.status_code == 200
    

    # Delete the value
    response = client.delete(f'/api/delete-product/{response.json["data"][0]["id"]}')
    assert response.status_code == 200
    

    # Verify the value is deleted
    response = client.get('/api/get-all')
    assert response.status_code == 200
    data = response.json['data']
    assert all(item['id'] != response.json['data'][0]['id'] for item in data)
