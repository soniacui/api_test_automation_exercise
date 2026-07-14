import httpx

# APIClient is a simple wrapper around the httpx library to facilitate making HTTP requests to a base URL.

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.client = httpx.Client(base_url=self.BASE_URL, timeout=10)

    def get(self, endpoint, **kwargs):
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.client.post(endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.client.put(endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.client.patch(endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.client.delete(endpoint, **kwargs)