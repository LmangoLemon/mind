import logging
from time import sleep

from cct.case import Case

logger = logging.getLogger(__file__)

class start_io(Case):

    def pre_test(self):
        logger.info ('doing something before start io')
        sleep(3)

    def process(self):
        logger.info('started io')
        sleep(5)
