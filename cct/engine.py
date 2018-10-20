import threading
import time


class Engine(object):

    def __init__(self, *keys, **kwargs):
        self.__testset = kwargs.get('test_set')
        self.__case_thread_list = []

    def start(self):
        # execute the cases
        for id,case in self.__testset.case_dict.items():
            t = threading.Thread(target=self.run_single_case(case), name=case.case_id)
            t.setDaemon(True)
            self.__case_thread_list.append(t)

        for t in self.__case_thread_list:
            t.start()


    def run_single_case_in_a_single_thread(self):
        pass

    def run_single_case(self, case):
        case.pre_test()
        case.pause()
        case.process()
        case.post_test()


def do1():
    print ("i am doing 1")


