import jsonschema
import json


class Validator:

    def validate_api_result_schema(self, result_api):
        with open("./Data/Schemas/api_result_schema.json") as schema_file:
            schema = json.load(schema_file)
        try:
            json_file = json.loads(result_api)
            jsonschema.validate(json_file, schema)
            result = True
        except Exception as e:
            result = e

        assert result is True, result
