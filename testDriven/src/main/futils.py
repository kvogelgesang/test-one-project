__author__ = 'kvogelgesang'

import os

class Futils:

    def __init__(self):
        self

    def get_resource_dir(self):
        return "%s/resources" % os.getcwd()

    def is_readable(self,dir):
        if os.access(dir, os.R_OK):
            return True
        else:
            return False

    def is_writeable(self,dir):
        if os.access(dir, os.W_OK):
            return True
        else:
            return False


#mytest=Futils()
#print mytest.get_base_dir()

