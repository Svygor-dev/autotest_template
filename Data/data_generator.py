from Data.Models.smoke_case_model import SmokeCase
import json


class DataGenerator:
    """
    Класс, отвечающий за генерацию/загрузку данных тест-кейсов
    """

    @staticmethod
    def get_smoke_data():
        """
        Метод загружает из json-файла данные для somke-тестов
        :return:
        """

        """Открываем json-файл"""
        with open("./Data/Cases/cases_smoke.json", "r",
                  encoding='utf-8') as read_file:
            """считываем его содержимое как json"""
            data = json.load(read_file)
            """Считываем json как массив объектов класса SmokeCase"""
            data = [SmokeCase(x) for x in data]

        return data
