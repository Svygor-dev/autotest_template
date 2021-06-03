import pytest
from Data.data_generator import DataGenerator
from TestHelpers.pre_processor import PreProcessor
from TestHelpers.test_processor import TestProcessor
from TestHelpers.validator import Validator
from Services.reqres_api_service import ReqresApiClient
from dotenv import load_dotenv
from config import Config


"""
Этот модуль отвечает за подготовку к прогону тестов.
Тут описаны все фикстуры, которые будут использоваться тестами.
"""


def pytest_addoption(parser):
    """
    Метод, который добавляет возможность указать стенд при запуске тестов.
    То есть теперь запуская тесты командой pytest Tests/test_smoke.py
    можно также указать параметр --stand который, если не указан явно, принимает значение prod
    То есть можно теперь писать такую команду для запуска тестов:
      pytest Tests/test_smoke.py --stand=prod
    Лучше также заполнять атрибут help и указать в нём, какие значения может принимать добавленный параметр --stand.
    """
    parser.addoption(
        "--stand",
        default="prod",
        required=False,
        help="available stands: prod"
    )


@pytest.fixture(scope="session", autouse=True)
def set_enviroment(request):
    """
    Фикстура, которая выполняется 1 раз за всю тестовую сессию и смысл её состоит в том,
        чтобы подгрузить нужные значения из файлов с описанием окружения.
    В примере есть только окружение prod, но в реальных проектах зачастую есть несколько стендов
        и именно внутри этого метода по значению, переданному в --stand при запуске тестов определяется,
        данные из какого файла будут использоваться в тестах.
    """
    stand = request.config.getoption("--stand")
    if stand == "prod":
        load_dotenv(dotenv_path="./Envs/prod.env")

    """А тут вызывается метод настройки тестового окружения. Подробнее, что это описано в файле config.py"""
    Config.init_config()


@pytest.fixture
def pre_processor():
    """
    В этом методе создаётся экземпляр класса PreProcessor, который используется для подготовки текущего стенда к тестам.
    Также, если нужно каким-то образом настроить PreProcessor, то эта настройка будет осуществляться
        в рамках этого метода (пример есть в методе test_processor() ниже)
    """
    pre_processor = PreProcessor()
    return pre_processor


@pytest.fixture
def test_processor():
    """
    В этом методе создаётся экземпляр класса TestProcessor, который используется для имитации действий пользователя.
    Также, если нужно каким-то образом настроить TestProcessor, то эта настройка будет осуществляться
        в рамках этого метода. Например TestProcessor использует в своей работе ReqresApiClient. Соответственно
        нужно в TestProcessor передать экземпляр этого сервиса и задать url_base сервиса, чтобы он отправлял запросы
        по тому адресу, который сейчас указан в конфигах
    """
    test_processor = TestProcessor()
    test_processor.reqres_api_service = ReqresApiClient()
    test_processor.reqres_api_service.url_base = Config.REQRES_API_URL
    return test_processor


@pytest.fixture
def validator():
    """
    В этом методе создаётся экземпляр класса Validator, который используется для проверки результата выполнения теста.
    Также, если нужно каким-то образом настроить Validator, то эта настройка будет осуществляться
        в рамках этого метода (пример есть в методе test_processor() выше)
    """
    fixture = Validator()
    return fixture


def pytest_generate_tests(metafunc):
    """
    Этот метод отвечает за реализацию DDT (Data Driven Testing).
    В случае если в тесте указана фикстура data_smoke, то из генератора вызывается метод по получению данных
        для смоук-тестов
    """
    for fixture in metafunc.fixturenames:
        if fixture == "data_smoke":
            generator = DataGenerator()
            test_data = generator.get_smoke_data()
            """
            Ниже настраивается параметризация тестов. В кавычках кказывается, как будет называться параметр
                с тестовыми данными текущего кейса, вторым параметром передаётся массив тест-кейсов,
                а параметр ids отвечает за то, каким будет название теста в отчете
            """
            metafunc.parametrize("data_smoke", test_data, ids=[str(x) for x in test_data])
