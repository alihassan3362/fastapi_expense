
from fastapi.testclient import TestClient
from main import app



client = TestClient(app)

def test_post_data():
    response = client.post("/categories/")
    assert response.status_code == 422

    
def test_get_data():
    response = client.get("/categories/")
    assert response.status_code == 200
    
def test_put_data():
    response = client.put("/categories/")
    assert response.status_code == 422
    
def test_delete_data():
    response = client.delete("/categories/")
    assert response.status_code == 422
    
# def test_get_data():
#     response = client.post("/categories/")
#     assert response.status_code == 422