from Data.Models.smoke_case_model import SmokeCase
import json


class DataGenerator:

    @staticmethod
    def get_smoke_data():

        with open("./Data/Cases/cases_smoke.json", "r",
                  encoding='utf-8') as read_file:
            data = json.load(read_file)
            data = [SmokeCase(x) for x in data]

        return data
