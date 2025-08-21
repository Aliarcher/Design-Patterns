"""
    Builder
    - Builder is a creational design pattern that lets you construct complex object setep by step.
    The pattern allows you to produce different types and representations of an object using the same
    construction code

"""
#Way 1
import abc
#Builder
class Car:
    def __init__(self):
        self_wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self,wheel):
        self._wheel = wheel

    def set_body(self,body):
        self._body = body

    def set_engine(self,engine):
        self._engine = engine

    def detail(self):
        print(f'Body: {self._body.shape}')
        print(f'Engine:{self._engine.hp}')
        print(f'Wheel:{self._wheel.seize}') 

# Parts
class Wheel: size = None
class Body: shape = None
class Engine: hp = None

class AbstractBuilder(abc.ABC): #Abstract Builder

    @abc.abstractmethod
    def get_engine(self):pass

    @abc.abstractmethod
    def get_wheel(self):pass

    @abc.abstractmethod
    def get_body(self):pass

class Benz(AbstractBuilder): # Concrete Builder 1
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return Wheel
    
    def get_body(self):
       body = Body()
       body.shape = 'Suv'
       return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    
class Bmw(AbstractBuilder): # Concrete Builder 2
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return Wheel
    
    def get_body(self):
       body = Body()
       body.shape = 'Sedan'
       return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine
    
#Director
class Director:
    _builder = None

    def set_builder(self,builder):
        self._builder = builder

    def construct(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)  

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        return car

#client
def client_builder(builder):
    builder = {
        'bmw':Bmw,
        'benz':Benz
    } 

    car = builder[builder]()
    director = Director()
    director.set_builder(car)
    result = director.construct()

    return result.detail()  

#test
client_builder('benz')
client_builder('bmw')


#Way2 Fluent (method chaining style)
import abc

# Product
class Car:
    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel):
        self._wheel = wheel
        return self   # ✅ method chaining

    def set_body(self, body):
        self._body = body
        return self   # ✅ method chaining

    def set_engine(self, engine):
        self._engine = engine
        return self   # ✅ method chaining

    def detail(self):
        print(f'Body: {self._body.shape}')
        print(f'Engine: {self._engine.hp}')
        print(f'Wheel: {self._wheel.size}')        


# Parts
class Wheel:
    size = None

class Body:
    shape = None

class Engine:
    hp = None


# Abstract Builder
class AbstractBuilder(abc.ABC):
    @abc.abstractmethod
    def get_engine(self): pass

    @abc.abstractmethod
    def get_wheel(self): pass

    @abc.abstractmethod
    def get_body(self): pass


# Concrete Builder 1
class Benz(AbstractBuilder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel   # ✅ must return object, not class

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine


# Concrete Builder 2
class Bmw(AbstractBuilder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine


# Director
class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        car = Car()
        # Fluent chaining style
        return (car
                .set_body(self._builder.get_body())
                .set_wheel(self._builder.get_wheel())
                .set_engine(self._builder.get_engine()))


# Client
def client_builder(builder_name):
    builders = {
        'bmw': Bmw,
        'benz': Benz
    }

    if builder_name not in builders:
        raise ValueError("Unknown builder name")

    builder = builders[builder_name]()  # instantiate builder
    director = Director()
    director.set_builder(builder)
    car = director.construct()
    car.detail()


# Test
client_builder('benz')
client_builder('bmw')



