__author__ = 'kvogelgesang'

import unittest
import os
import sys
sys.path.append("../main")
import futils

class FutilsTests(unittest.TestCase):

    global RESOURCE_DIR
    RESOURCE_DIR = "%s/resources" % os.getcwd()

    def testGetResourceDir(self):
        mytest=futils.Futils()
        self.assertEquals(mytest.get_resource_dir(), RESOURCE_DIR, "testGetResourceDir failed!")

    def testIsReadable(self):
        mytest=futils.Futils()
        self.assertEquals(mytest.is_readable(RESOURCE_DIR) ,True, "testIsReadable failed!")

    def testIsWriteable(self):
        mytest=futils.Futils()
        self.assertEquals(mytest.is_writeable(RESOURCE_DIR) ,True, "testIsWriteable failed!")



if __name__ == '__main__':
    unittest.main()