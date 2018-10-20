from time import sleep

from cct.case import Case


class create_lun(Case):


    def pre_test(self):
        print ('doing something before create luns')
        sleep(3)

    def process(self):
        print('create luns')
        sleep(5)







