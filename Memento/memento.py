"""
memnto Version control
"""

from string import ascii_letters
from random import sample
import abc
from datetime import datetime

class Orginator:
    _state = None


    def __init__(self , state):
        self._state = state
        print(f'Orginator: My initial state is: {self._state}')

    def do_something(self):
        print('Orginator: I am doing something important.')
        self._state = self._generate_random_string(30)
        print(f'Orginator: my state has changed to: {self._state}')

    def _generate_random_string(self, length):
        return ''.join(sample(ascii_letters,length))
    
    def save(self):
        return ConcreteMemento(self._state)
    
    def restore(self, memento):
        self._state = memento.get_state()
        print(f'Orginator: state has changed to: {self._state}')

    
class Memento(abc.ABC):


    @abc.abstractclassmethod
    def get_name(self):
        pass


    @abc.abstractclassmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):

    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())

    def get_state(self):
        return self._state
    
    def get_name(self):
        return f'{self._date} / {self._state}'
    
    def get_date(self):
        return str(self._date)
    
class Caretaker:

    def __init__(self , orginator):
        self._orginator = orginator

        self._mementos = []

    def backup(self):
        print('\nCareTaker: saving orginator state...')
        self._mementos.append(self._orginator.save())

    
    def undo(self):
        if not len(self._mementos):
            return None
        
        memento = self._mementos.pop()
        print(f'Caretaker: Restoring state to: {memento.get_name()} ')
        try:
            self._orginator.restor(memento)
        except Exception:
            self.undo()


    def show_history(self):
        print('Caretaker: here is the list of mementos: ')
        for memento in self._mementos:
            print(memento.get_name())


orginator = Orginator('first-name')
caretaker = Caretaker(orginator)

caretaker.backup()
orginator.do_something()

caretaker.backup()
orginator.do_something()

caretaker.backup()
orginator.do_something()


print()
caretaker.show_history()