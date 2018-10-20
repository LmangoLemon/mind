class TestSet(object):

    def __init__(self, case_dict):
        self.__case_dict = case_dict

    @property
    def case_dict(self):
        return self.__case_dict
