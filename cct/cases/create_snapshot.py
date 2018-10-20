from time import sleep

from cct.case import Case


class create_snapshot(Case):


    def pre_test(self):
        print ('doing something before create snapshot')
        sleep(3)

    def process(self):
        print('create snapshot')
        sleep(5)







