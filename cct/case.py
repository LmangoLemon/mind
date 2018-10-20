import threading
import time


class Case(object):

    def __init__(self, case_id):
        self.__case_id = case_id
        self.__signal = threading.Event()
        self.__status='init'

    def resume(self):
        self.__signal.set()

    @property
    def case_id(self):
        return self.__case_id

    def pre_test(self):
        print("模拟前置步骤，直接睡眠3s")
        time.sleep(3)
        pass

    def process(self):
        self.do_something_before_pause()
        self.__signal.wait()
        pass

    def post_test(self):
        pass

    def do_something_before_pause(self):
        print('doing something before pause myself')
        pass
