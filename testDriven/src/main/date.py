'''
Created on Mar 12, 2012

@author: KVogelgesang
'''
import datetime

class Date:
    
    def __init__(self):
        self
        
    def mydatetime(self):
        return datetime.datetime.now()
    
    def dateonly(self):
        return str(self.mydatetime()).split(' ',1)[0] 
    
    def timeonly(self):
        return str(self.mydatetime()).split(' ',1)[1] 
    
    def formatDateonly(self,string):
        datearray = str(string).split('-',2)
        return "%s.%s.%s" % (datearray[2],datearray[1],datearray[0]) 
    
    def formattimeonly(self,string):
        firstarray = str(string).split('.',1)
        secondarray = firstarray[0].split(':',2)
        return "%s:%s" % (secondarray[0],secondarray[1])
         
        

#if __name__ == '__main__':
    #mydate = Date()
    #print mydate.formatDateonly(str(mydate.dateonly()))
    #print mydate.mydatetime()
    #print mydate.formattimeonly(str(mydate.timeonly()))



        