__author__ = 'kvogelgesang'

import unittest
import os
import sys
sys.path.append("../main")
import futils

class FutilsTests(unittest.TestCase):

    global RESOURCE_DIR
    RESOURCE_DIR = "%s/resources" % os.getcwd()

    def testnewestversion(self):
        mytest=futils.Futils()
        self.assertEquals(mytest.get_resource_dir(),RESOURCE_DIR, "test failed!")


if __name__ == '__main__':
    unittest.main()