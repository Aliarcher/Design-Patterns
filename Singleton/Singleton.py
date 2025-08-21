"""
    Singletone
        -Ensure a class only has one instace, and provide a global point of access to it

"""

#Way 1 (without meta class)
class A:
    _instance = None
    def __init__(self):
        raise RuntimeError('call get_instance() instead')
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


try:
  #This reaise error
  a_instance = A()
#This is correct        
except:
    a_instance = A.get_instance()
    b_instance = A.get_instance()
    print(id(a_instance))    
    print(id(b_instance))

#Way 2 (use meta class)
#Reusable
class Singleton(type):

    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            return super().__call__(*args, **kwds)
        return self._instance    
    
class B(metaclass=Singleton):
    pass

a_instance = B()
b_instance = B()

print(id(a_instance))
print(id(b_instance))

