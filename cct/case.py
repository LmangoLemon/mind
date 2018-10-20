import logging
import threading
import time

from cct.common.enums import case_running_status

logger = logging.getLogger(__file__)

class Case(object):

    def __init__(self, case_id, case_name, dependence, process_at):
        self.__case_id = case_id
        self.__signal = threading.Event()
        self.__status = case_running_status.INIT
        self.__name = case_name
        self.__dependence = dependence
        self.__operation_status = None
        self.__dependence_op = process_at
        self.__test_set = None

    @property
    def test_set(self):
        return self.__test_set

    @test_set.setter
    def test_set(self, ts):
        self.__test_set = ts

    @property
    def dep_op_dict(self):
        return self.__dependence_op

    @property
    def operation_status(self):
        return self.__operation_status

    @operation_status.setter
    def operation_status(self, status):
        self.__operation_status = status

    @property
    def dependence(self):
        return self.__dependence

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def name(self):
        return self.__name

    def resume(self):
        logger.info('case={id} is resumed'.format(id=self.name))
        self.__signal.set()

    def pause(self):
        logger.info('case={id} is paused'.format(id=self.name))
        self.__signal.clear()
        self.__signal.wait()

    @property
    def case_id(self):
        return self.__case_id

    def pre_test(self):
        logger.info("do something before test")
        time.sleep(3)
        pass

    def process(self):
        pass

    def post_test(self):
        pass

    def set_case_operation_status(self, status):
        self.test_set.set_case_operation_status(self, status)
