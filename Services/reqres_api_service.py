import requests


class ReqresApiClient:
    """
    Класс, отвечающий за работу с API reqres
    """

    """Адрес тестируемого API"""
    url_base = None

    def __new__(cls):
        """
        Реализация singleton.
        Суть в том, что если у класса уже существует атрибут instance, то мы просто возвращаем его.
        Если же у класса атрибута instance нет, то мы создаём instance, который будет содержать
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ReqresApiClient, cls).__new__(cls)
        return cls.instance

    def get_user(self, user_id):
        """
        Метод отправки запроса по получению пользователя по user_id
        :param user_id: id пользователя
        :return: ответ от API
        """
        get_user_url = self.url_base + "/api/users"
        payload = {"id": user_id}
        response = requests.get(get_user_url, params=payload)
        return response
