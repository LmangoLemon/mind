from time import sleep

from cct.case import Case


class start_io(Case):

    def pre_test(self):
        print ('doing something before start io')
        sleep(3)

    def process(self):
        print('started io')
        sleep(5)
