class SmokeCase:

    user_id = None
    test_name = None

    def __init__(self, dictionary=None, test_name=None, user_id=None):
        if dictionary is not None:
            self.__dict__ = dictionary
        else:
            self.user_id = user_id
            self.test_name = test_name

    def __str__(self):
        return self.test_name

