from time import sleep

from cct.case import Case
from cct.common.enums import case_operation_status


class create_lun(Case):

    def pre_test(self):
        print ('doing something before create luns')
        sleep(3)

    def process(self):
        self.set_case_operation_status(case_operation_status.PRE)
        print('create luns')

        sleep(5)

        self.set_case_operation_status(case_operation_status.POST)

    def post_test(self):
        print('create lun has finished')
