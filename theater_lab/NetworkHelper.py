import requests

class NetworkHelper:
    BASE_URL = "http://127.0.0.1:8000/api/"

    @staticmethod
    def get_list(endpoint):
        response = requests.get(f"{NetworkHelper.BASE_URL}{endpoint}/")
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Error: Response is not valid JSON.")
                return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    @staticmethod
    def get_item(endpoint, item_id):
        response = requests.get(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/")
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def delete_item(endpoint, item_id):
        response = requests.delete(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/")
        return response.status_code == 204

    @staticmethod
    def create_item(endpoint, data):
        response = requests.post(f"{NetworkHelper.BASE_URL}{endpoint}/", data=data)
        return response.status_code == 201

    @staticmethod
    def update_item(endpoint, item_id, data):
        response = requests.put(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/", data=data)
        return response.status_code == 200

