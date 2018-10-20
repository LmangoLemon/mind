import threading
import time


class Case(object):

    def __init__(self, case_id,case_name):
        self.__case_id = case_id
        self.__signal = threading.Event()
        self.__status = 'init'
        self.__name=case_name

    @property
    def name(self):
        return self.__name

    def resume(self):
        print('case={id} is resumed'.format(id=self.case_id))
        self.__signal.set()

    def pause(self):
        print('case={id} is paused'.format(id=self.case_id))
        self.__signal.clear()

    @property
    def case_id(self):
        return self.__case_id

    def pre_test(self):
        print("do something before test")
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
