class TestProcessor:

    reqres_api_service = None

    def send_request(self, user_id):
        result = self.reqres_api_service.get_user(user_id)
        return result
