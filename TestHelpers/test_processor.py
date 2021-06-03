class TestProcessor:
    """
    Используется для имитации действий пользователя.
    В этом классе будут методы по отправке запросов, цепочек запросов, ожиданию/получению ответов
        и другие действия, которые выполняет пользователь с тестируемой системой.
    """

    reqres_api_service = None

    def send_request(self, user_id):
        """
        Метод отправки запроса по получению пользователя по user_id
        :param user_id: id пользователя
        :return: ответ от API
        """
        result = self.reqres_api_service.get_user(user_id)
        return result
