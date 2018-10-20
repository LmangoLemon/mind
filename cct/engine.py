
import threading
import time


class Engine(object):

    def start(self):
        # execute the cases
        pass




    def run_single_case_in_a_single_thread(self):
        pass

    def run_single_case(self, case):
        case.pre_test()
        if case.can_run():
            case.process()
        case.post_test()

def do1():
    print ("i am doing 1")


def test():
    threading.Thread(target=loop, name='LoopThread')



