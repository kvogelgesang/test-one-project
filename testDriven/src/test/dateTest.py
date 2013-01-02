'''
Created on Mar 12, 2012

@author: KVogelgesang
'''
import unittest
import datetime
import sys
sys.path.append("../main")
import date

class DateTests(unittest.TestCase):
    
    def testdateformat(self):
        mydate = date.Date()
        #self.failUnless(mytry.matches(myexpect))
        self.assertEquals(mydate.formatDateonly("2013-01-03"), "03.01.2013", "dateformat test failed!")
        
    def testtimeformat(self):
        mydate = date.Date()
        self.assertEquals(mydate.formattimeonly("13:41:27.228651"), "13:41", "timeformat test failed!")

if __name__ == '__main__':
    unittest.main()
    
