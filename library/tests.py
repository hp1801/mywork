import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_book(client):
    book_data = {
        "title": "Test Book",
        "author": "Author A",
        "isbn": "12345",
        "publication_year": 2024
    }
    response = client.post('/books', json=book_data)
    assert response.status_code == 201

    book_id = response.get_json()['id']
    response = client.get(f'/books/{book_id}')
    assert response.status_code == 200
    assert response.get_json()['title'] == "Test Book"
