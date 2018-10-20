import logging
from time import sleep

from cct.case import Case




logger = logging.getLogger(__file__)

class create_snapshot(Case):

    def pre_test(self):
        logger.info ('doing something before create snapshot')
        sleep(3)

    def process(self):
        logger.info('create snapshot')
        sleep(5)

    def post_test(self):
        logger.info('create snapshot finished')
