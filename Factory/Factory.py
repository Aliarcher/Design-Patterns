"""
    Factory
    - Factory is a creational design pattern that provides an interface for creating objects
      in a superclass,but allows subclassess to alter the type of objects that will be created

    3 component => 1.Creator 2.Prodcut 3.Client
"""
from abc import ABC,abstractmethod

class File(ABC): #Creator
    def __init__(self,file):
        self.file = file
    @abstractmethod
    def make(self):
        pass
    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result
             

class Json: # Product
    def edit(self,file):
        return f'Working on {file} Json...'
    
class Xml: # Product
    def edit(self,file):
        return f'Working on {file} xml'    
    
class JsonFile(File): #Creator
    def make(self):
        return Json()

class XmlFile(File): #Creator
    def make(self):
        return Xml()   
    

def Developer(file,format): # Client
    format={
        'json':JsonFile,
        'xml':XmlFile
    }    
    result = format[format](file)

    return result.call_edit()

print(Developer('show','json'))
print(Developer('show','xml'))