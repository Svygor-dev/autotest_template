import pytest
from Data.data_generator import DataGenerator
from TestHelpers.pre_processor import PreProcessor
from TestHelpers.test_processor import TestProcessor
from TestHelpers.validator import Validator
from Services.reqres_api_service import ReqresApiClient
from dotenv import load_dotenv
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--stand",
        required=False
    )


@pytest.fixture(scope="session", autouse=True)
def set_enviroment(request):
    stand = request.config.getoption("--stand")
    if stand == "prod":
        load_dotenv(dotenv_path="./Envs/prod.env")
    Config.init_config()


@pytest.fixture
def pre_processor():
    pre_processor = PreProcessor()
    return pre_processor


@pytest.fixture
def test_processor():
    test_processor = TestProcessor()
    test_processor.api_service_client = ReqresApiClient()
    return test_processor


@pytest.fixture
def validator():
    fixture = Validator()
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture == "data_smoke":
            generator = DataGenerator()
            test_data = generator.get_smoke_data()
            metafunc.parametrize("data_smoke", test_data, ids=[str(x) for x in test_data])
