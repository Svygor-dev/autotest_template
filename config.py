import os


class Config:
    """
    Класс, который содержит в себе все конфиги.
    Другие классы будут обращаться к нему, а не напрямую к переменным окружения
        для получения таких данных, как адрес текущего стенда, адрес БД и т.д.
    Нужен для того, чтобы в случае изменения имени или способа получения параметра окружения обращение к нему
        нужно было бы менять в 1 месте, а не в каждом классе/методе, для которого этот параметр окружения важен.
    """

    """Перечисляем все переменные, которые нам нужны"""
    REQRES_API_URL = None

    @classmethod
    def init_config(cls):
        """
        Присваиваем значения переменным класса из соответствующих переменных среды
            или другим способом их определяем.
        """
        cls.REQRES_API_URL = os.environ.get("REQRES_API_URL")
