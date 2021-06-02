import requests


class ReqresApiClient:

    url_base = "https://reqres.in"

    def get_user(self, user_id):
        get_user_url = self.url_base + "/api/users"
        payload = {"id": user_id}
        response = requests.get(get_user_url, params=payload)
        return response
