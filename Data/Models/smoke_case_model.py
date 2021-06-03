class SmokeCase:
    """
    Класс, описывающий тест-кейс для smoke-теста
    """

    user_id = None
    test_name = None
    expected_status_code = None

    def __init__(self, dictionary=None, test_name=None, user_id=None, expected_status_code=None):
        """
        При создании объекта класса SmokeCase можно либо передать каждый параметр отдельно, либо
            передать сразу словарь со значениями, которые должен содержать текущий тест-кейс
        :param dictionary: словарь со всеми необходимыми для кейса значениями
        :param test_name: название теста
        :param user_id: id пользователя
        :param expected_status_code: ожидаемый статус-код, который должен вернуться при запросе пользователя по user_id
        """
        if dictionary is not None:
            self.__dict__ = dictionary
        else:
            self.user_id = user_id
            self.test_name = test_name
            self.expected_status_code = expected_status_code

    def __str__(self):
        """
        Переопределяем метод преобразования объекта в строку таким образом, чтобы
            при попытке представить объект в виде строки возвращалось имя теста.
        :return:
        """
        return self.test_name

