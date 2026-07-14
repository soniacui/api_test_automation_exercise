import httpx
import json

RESOURCES = ["posts", "comments", "albums", "photos", "todos", "users"]

CREATE_PAYLOADS = {
    "posts": {"title": "Post title", "body": "Post body", "userId": 1},
    "comments": {
        "name": "Comment name",
        "email": "qa@example.com",
        "body": "Comment body",
        "postId": 1,
    },
    "albums": {"title": "Album title", "userId": 1},
    "photos": {
        "title": "Photo title",
        "url": "https://example.com/photo.jpg",
        "thumbnailUrl": "https://example.com/thumb.jpg",
        "albumId": 1,
    },
    "todos": {"title": "Todo title", "completed": False, "userId": 1},
    "users": {
        "name": "Jane Doe",
        "username": "janedoe",
        "email": "jane@example.com",
    },
}

PUT_PAYLOADS = {
    "posts": {"id": 1, "title": "Updated post", "body": "Updated body", "userId": 1},
    "comments": {
        "id": 1,
        "name": "Updated comment",
        "email": "updated@example.com",
        "body": "Updated comment body",
        "postId": 1,
    },
    "albums": {"id": 1, "title": "Updated album", "userId": 1},
    "photos": {
        "id": 1,
        "title": "Updated photo",
        "url": "https://example.com/updated-photo.jpg",
        "thumbnailUrl": "https://example.com/updated-thumb.jpg",
        "albumId": 1,
    },
    "todos": {"id": 1, "title": "Updated todo", "completed": True, "userId": 1},
    "users": {
        "id": 1,
        "name": "Updated Jane",
        "username": "updatedjane",
        "email": "updated-jane@example.com",
    },
}

PATCH_PAYLOADS = {
    "posts": {"title": "Patched post"},
    "comments": {"name": "Patched comment"},
    "albums": {"title": "Patched album"},
    "photos": {"title": "Patched photo"},
    "todos": {"completed": True},
    "users": {"name": "Patched Jane"},
}

BASE_URL = "https://jsonplaceholder.typicode.com"

results = {
    "GET": {},
    "POST": {},
    "PUT": {},
    "PATCH": {},
    "DELETE": {}
}

with httpx.Client() as client:
    # GET
    for r in RESOURCES:
        resp = client.get(f"{BASE_URL}/{r}/1")
        results["GET"][r] = {
            "status_code": resp.status_code,
            "response_json": resp.json()
        }
    
    # POST
    for r in RESOURCES:
        payload = CREATE_PAYLOADS[r]
        resp = client.post(f"{BASE_URL}/{r}", json=payload)
        results["POST"][r] = {
            "status_code": resp.status_code,
            "response_json": resp.json()
        }

    # PUT
    for r in RESOURCES:
        payload = PUT_PAYLOADS[r]
        resp = client.put(f"{BASE_URL}/{r}/1", json=payload)
        results["PUT"][r] = {
            "status_code": resp.status_code,
            "response_json": resp.json()
        }

    # PATCH
    for r in RESOURCES:
        payload = PATCH_PAYLOADS[r]
        resp = client.patch(f"{BASE_URL}/{r}/1", json=payload)
        results["PATCH"][r] = {
            "status_code": resp.status_code,
            "response_json": resp.json()
        }

    # DELETE
    for r in RESOURCES:
        resp = client.delete(f"{BASE_URL}/{r}/1")
        results["DELETE"][r] = {
            "status_code": resp.status_code,
            "response_json": resp.json()
        }

print(json.dumps(results, indent=2))
