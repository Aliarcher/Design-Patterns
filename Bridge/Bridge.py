"""
    Bridge
    - a structural design pattern that lets you split a large class into seperate
    hierarchies - abstraction and implementation - which can be developed independently of each other
"""
import abc

class Shape(abc.ABC): # Abstraction
    def __init__(self,color):
        self._color = color
    def show(self):
        pass

class Circle(Shape): # Refined Abstraction
    def show(self):
        self._color.paint(self.__class__.__name__)

class Square(Shape): # Refined Abstraction
    def show(self):
        self._color.paint(self.__class__.__name__)

class Triangle(Shape): # Refined Abstraction
    def show(self):
        self._color.paint(self.__class__.__name__)

class Color(abc.ABC): #Implementation
    def paint(self,name):
        pass

class Blue(Color): # Concrete Implementation
    def paint(self, name):
        print(f'this is a blue {name}')  

class Red(Color): # Concrete Implementation
    def paint(self, name):
        print(f'this is a red {name}')

class Yellow(Color): # Concrete Implementation
    def paint(self, name):
        print(f'this is a yellow {name}')

red = Red()
blue = Blue()
yellow = Yellow()
circle = Circle(red)
circle.show()
triangle = Triangle(blue)
triangle.show()
square = Square(yellow)
square.show()