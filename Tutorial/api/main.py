import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# GET
def get_posts():
    response = requests.get(BASE_URL)
    print("\nGET ALL POSTS:")
    print(response.json()[:3])  # show only 3

# POST
def create_post():
    data = {
        "title": "Python API Project",
        "body": "Using GET POST PUT DELETE in Python",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=data)
    print("\nPOST CREATED:")
    print(response.json())

# PUT
def update_post():
    data = {
        "title": "Updated Title",
        "body": "Updated using PUT method",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/1", json=data)
    print("\nPUT UPDATED:")
    print(response.json())

# DELETE
def delete_post():
    response = requests.delete(f"{BASE_URL}/1")
    print("\nDELETE STATUS:")
    print(response.status_code)

if __name__ == "__main__":
    get_posts()
    create_post()
    update_post()
    delete_post()
