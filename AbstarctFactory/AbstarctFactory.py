"""
    Abstract Factory
    - Abstract Factory Patter serves to provide an interface for creating related/dependent
    objects without need to specify their actual class

    Car => Benz Bmw => Suv, Coupe
           benz suv => gla
           bmw suv  => x1
           benz coupe => cls
           bmw coupe => m2

    Notice:
        Abstract(methods not implememnted) != Concrete (methods implemented)           
"""

from abc import ABC, abstractmethod

#Factory

class Car(ABC): #Abstact Factory
    @abstractmethod
    def call_suv(self):
        pass
    @abstractmethod
    def call_coupe(self):
        pass

#ConcreteFactory
class Benz(Car): #Concrete Factory 1
    def call_suv(self):
        return Gla()
    def call_coupe(self):
        return Cls()
    
class Bmw(Car): #Concrete Factory 2
    def call_suv(self):
        return X1()
    def call_coupe(self):
        return M2()   

#product

#Abstact
class Suv(ABC): #Abstarct Product A
    @abstractmethod
    def create_suv(self):
        pass
class Coupe(ABC): #Abstarct Product B
    @abstractmethod
    def  create_coupe(self):
        pass

#Concrete
class Gla(Suv): # Concrete Product A1
    def create_suv(self):
        print('This is your suv benz gla...') 
class X1(Suv): # Concrete Product A2
    def create_suv(self):
        print('This is your suv bmw x1...')

class Cls(Coupe): # Concrete Product B1
    def create_coupe(self):
        print('This is your coupe benz cls...')
class M2(Coupe): # Concrete Product B2
    def create_coupe(self):
        print('This is your coupe bmw m2 ...')        


#client
def client_suv(order): # Client 1
    brands = {
        'benz': Benz,
        'bmw': Bmw
    }
    suv = brands[order]().call_suv()
    suv.create_suv()

def client_coupe(order): # Client 2
    brands ={
        'benz': Benz,
        'bmw': Bmw
    }
    coupe = brands[order]().call_coupe()
    coupe.create_coupe()   

#Test
client_coupe('benz')
client_coupe('bmw')
client_suv('benz')

client_suv('bmw')  
