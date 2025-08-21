"""
    Prototype
    - Prototype is a creational design pattern that lets you copy existing objects
    without making your code dependant on their classess.

    Notice:
        copy.copy(x):
            Return a shallow copy of x
        copy.deepcopy(x[,memo])
            Return a deep copy of x    

"""
import copy

#Prototype
class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self,name,obj):
        self._objects[name] = obj

    def unregister(self,name):
        del self._objects[name]

    def clone(self,name,**kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)  
        return cloned_obj          

#client
def client_prototype(name,obj,**kwargs):
    prototype = Prototype()
    prototype.register(name,obj)
    return prototype.clone(name,**kwargs)


#Test
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('Ali',29)

p_clone = client_prototype('Person 1',p)

print(p_clone.__dict__)
print(id(p))
print(id(p_clone))
print(id(p_clone.age))

#change age

p_clone1 = client_prototype('Person 1',p,age=28)

print(p_clone1.__dict__)
print(id(p_clone1))
print(id(p_clone1.age))

#copy from p_clone1

p_clone2 = client_prototype('Person 2',p_clone1,age=19)

print(p_clone2.__dict__)
print(id(p_clone2))
print(id(p_clone2.age))
