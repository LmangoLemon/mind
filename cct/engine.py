import threading
import time

from cct.common.enums import case_running_status


class Engine(object):

    def __init__(self, *keys, **kwargs):
        self.__testset = kwargs.get('test_set')
        self.__case_thread_list = []

    def start(self):
        # execute the cases
        for id, case in self.__testset.case_dict.items():
            t = threading.Thread(target=self.run_single_case, name=case.case_id, kwargs={'case': case})
            t.setDaemon(True)
            print('test case ={name} will start'.format(name=case.name))
            t.start()
            self.__case_thread_list.append(t)

        for t in self.__case_thread_list:
            t.join()
    def run_single_case(self, case):
        try:
            case.status = case_running_status.RUNNING
            self.pause_4_depend_other_case(case)
            case.pre_test()

            self.pause_4_depend_op_status(case)
            case.process()
            case.post_test()

            self.__testset.set_case_status(case, case_running_status.PASS)
        except:

            self.__testset.set_case_status(case, case_running_status.FAILED)

    def pause_4_depend_other_case(self, case):
        if case.dependence:
            print('case={name} will pause to wait for other case running status'.format(name=case.name))
            case.pause()

    def pause_4_depend_op_status(self, case):
        if case.dep_op_dict:
            print('case={name} will pause to wait for other case op status'.format(name=case.name))
            case.pause()
        else:
            print ('case={name} will not pause={rst}'.format(name=case.name, rst=case.dep_op_dict is None))


def do1():
    print ("i am doing 1")
