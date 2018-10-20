class TestSet(object):

    def __init__(self, case_dict):
        self.__case_dict = case_dict
        self.__case_running_status_dict = {}
        self.__case_dep_running_status_dict = {}
        self.__case_dep_op_status_dict = {}
        self.__load_data()
        self.__load_data(False)

        for id, case in self.case_dict.items():
            case.test_set = self

    @property
    def case_dict(self):
        return self.__case_dict

    def __load_case_dependence_relation(self):
        '''
        add caseId_status: case_list to local dict
        :return:
        '''
        for case_id, case in self.case_dict.items():
            depend_case_id = case.dependence.get('id')
            op_dep_case_id = case.__dependence_process_at.get('id')
            op_dep_status = case.__dependence_op('status')
            key = '{case_id}_{status}'.format(case_id=depend_case_id,
                                              status=case.dependence.get('status').upper())
            key_operation = '{case_id}_{status}'.format(case_id=op_dep_case_id,
                                                        status=op_dep_status.upper())

            case_list = self.__case_dep_running_status_dict.get(
                key) if key in self.__case_dep_running_status_dict else []
            case_list.append(case)
            if key in self.__case_dep_running_status_dict:
                self.__case_dep_running_status_dict[key] = case_list

            case_op_dep_list = self

    def __load_data(self, is_dep_running=True):
        target_dict = self.__case_running_status_dict if is_dep_running else self.__case_dep_op_status_dict
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

        cases = self.__case_running_status_dict.get(key)
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
