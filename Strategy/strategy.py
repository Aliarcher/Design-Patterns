import abc


class Read:

    def __init__(self, sentence):
        self.sentence = sentence
        self._direction = None # strategy instance

    
    def set_sirection(self, direction):
        self._direction = direction

    def read(self):
        return self._direction.direct(self.sentence)
    


class Direction(abc.ABC):  # Abstract Strategy

    @abc.abstractclassmethod
    def direct(self,data):
        pass



class Right(Direction): # Concrete Strategy

    def direct(self, data):
        print(data[::-1])

class Left(Direction): # Concrete Strategy

    def direct(self, data):
        print(data[::1])


c = Read('Hello seyyed!')
c.set_sirection(Right()) # Right strategy
c.read()



c.set_sirection(Left()) # Left strategy
c.read()