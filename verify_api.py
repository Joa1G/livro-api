import urllib.request
import urllib.parse
import json
import sys

BASE_URL = 'http://127.0.0.1:8000/api/livros/'

def make_request(url, method='GET', data=None):
    if data:
        data = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Content-Type', 'application/json')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status != 204:
                return json.loads(response.read().decode('utf-8')), response.status
            return None, response.status
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        print(e.read().decode('utf-8'))
        return None, e.code
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None, 0

def test_crud():
    # 1. Create
    print("Testing Create...")
    data = {
        "titulo": "O Senhor dos Anéis",
        "dataPublicacao": "29/07/1954",
        "edicao": "1"
    }
    response, status = make_request(BASE_URL, 'POST', data)
    if status == 201:
        print("Create Success:", response)
        book_id = response['id']
    else:
        print("Create Failed")
        return

    # 2. List
    print("\nTesting List...")
    response, status = make_request(BASE_URL, 'GET')
    if status == 200:
        print("List Success:", response)
    else:
        print("List Failed")

    # 3. Retrieve
    print(f"\nTesting Retrieve ID {book_id}...")
    response, status = make_request(f"{BASE_URL}{book_id}/", 'GET')
    if status == 200:
        print("Retrieve Success:", response)
    else:
        print("Retrieve Failed")

    # 4. Update
    print(f"\nTesting Update ID {book_id}...")
    update_data = {"titulo": "O Senhor dos Anéis - A Sociedade do Anel"}
    response, status = make_request(f"{BASE_URL}{book_id}/", 'PATCH', update_data)
    if status == 200:
        print("Update Success:", response)
    else:
        print("Update Failed")

    # 5. Delete
    print(f"\nTesting Delete ID {book_id}...")
    response, status = make_request(f"{BASE_URL}{book_id}/", 'DELETE')
    if status == 204:
        print("Delete Success")
    else:
        print("Delete Failed")

if __name__ == "__main__":
    test_crud()
