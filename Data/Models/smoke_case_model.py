class SmokeCase:

    user_id = None
    test_name = None
    expected_status_code = None

    def __init__(self, dictionary=None, test_name=None, user_id=None, expected_status_code=None):
        if dictionary is not None:
            self.__dict__ = dictionary
        else:
            self.user_id = user_id
            self.test_name = test_name
            self.expected_status_code = expected_status_code

    def __str__(self):
        return self.test_name

