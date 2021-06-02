def test_mmg_smoke(data_smoke, pre_processor, test_processor, validator):
    """Смоук-тесты
        data - данные о текущем кейсе
    """

    """
    Подготовка окружения к выполнению тестов.
    В примере метод ничего не делает, но сюда обычно входит чистка БД,
    различных хранилищ и другие действия для приведения стенда
    к состоянию, при котором можно начинать тестирование
    """
    pre_processor.clear_stand()

    """
    Основные действия теста.
    Именно в этом блоке происходит имитация действий пользователя.
    """
    result_api = test_processor.send_request(data_smoke.user_id)

    """
    Различные проверки.
    В этом примере всего 2 проверки:
     1) что вернулся код 200;
     2) проверка ответа по json-схеме
    """
    assert result_api.status_code == data_smoke.expected_status_code
    if data_smoke.expected_status_code == 200:
        validator.validate_api_result_schema(result_api.text)
