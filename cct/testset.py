class TestSet(object):

    def __init__(self, case_dict):
        self.__case_dict = case_dict
        self.__case_dep_running_status_dict = {}
        self.__case_dep_op_status_dict = {}
        self.__load_data()
        self.__load_data(False)

        for id, case in self.case_dict.items():
            case.test_set = self

    @property
    def case_dict(self):
        return self.__case_dict



    def __load_data(self, is_dep_running=True):
        target_dict = self.__case_dep_running_status_dict if is_dep_running else self.__case_dep_op_status_dict
        for id, case in self.case_dict.items():
            dep_dict = case.dependence if is_dep_running else case.dep_op_dict
            if dep_dict is not None:
                dep_id = dep_dict.get('id')
                status = dep_dict.get('status').upper()
                key = '{case_id}_{status}'.format(case_id=dep_id, status=status)

                if key not in target_dict:
                    target_dict[key] = []
                target_dict[key].append(case)

    def set_case_status(self, case, case_status):
        '''
        update case status, and send xxx
        :param case:
        :param case_status:
        :return:

        '''

        case.status = case_status
        # make the related case available
        key = '{case_id}_{status}'.format(case_id=case.case_id, status=case_status.key.upper())

        cases = self.__case_dep_running_status_dict.get(key)
        if cases:
            for dep_case in cases:
                dep_case.resume()

    def set_case_operation_status(self, case, status):
        case.operation_status = status

        key = '{case_id}_{status}'.format(case_id=case.case_id, status=status.key.upper())
        cases = self.__case_dep_op_status_dict.get(key)
        if cases:
            for dep_case in cases:
                dep_case.resume()
