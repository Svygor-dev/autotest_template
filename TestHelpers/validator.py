import jsonschema
import json


class Validator:
    """
    Класс, содержащий различные методы проверки результатов.
    Будут различные проверки по JSON-схемам, проверки конкретных значений в результатах и т.д.
    """

    def validate_api_result_schema(self, result_api):
        """
        Метод проверки результата ответа по json-схеме.
        :param result_api: текст ответа, который нужно проверить по схеме
        """

        """Загружаем json-схему из файла"""
        with open("./Data/Schemas/api_result_schema.json") as schema_file:
            schema = json.load(schema_file)
        try:
            "Проверяем, что результат соответствует json-схеме"
            json_file = json.loads(result_api)
            jsonschema.validate(json_file, schema)
            result = True
        except Exception as e:
            """В случае, если проверка по схеме не проходит, то оставляем """
            result = e
        """
        Проверяем, что в результате проверка по схеме успешно пройдена
        Если нет, то в качестве текста ошибки будет отображена ошибка, которую вернул метод
            jsonschema.validate()
        """
        assert result is True, result
