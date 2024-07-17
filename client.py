import requests

BASE_URL = "http://localhost:5000"

def login():
    response = requests.post(f"{BASE_URL}/login", json={"username": "test", "password": "test"})
    return response.json().get('access_token')

def get_item(token, item_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/item/{item_id}", headers=headers)
    return response.json()

def create_item(token, data):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/item", json=data, headers=headers)
    return response.json()

def update_item(token, item_id, data):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}/item/{item_id}", json=data, headers=headers)
    return response.json()

def delete_item(token, item_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/item/{item_id}", headers=headers)
    return response.json()

def health_check():
    response = requests.get(f"{BASE_URL}/health")
    return response.json()

if __name__ == '__main__':
    token = login()
    print("Health Check:", health_check())
    print("Create Item:", create_item(token, {"_id": "1", "name": "item1"}))
    print("Get Item:", get_item(token, "1"))
    print("Update Item:", update_item(token, "1", {"name": "updated item1"}))
    print("Delete Item:", delete_item(token, "1"))
