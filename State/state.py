import abc

class Elevator:
    _state = None

    def __init__(self, state):
        self.set_state(state)

    def set_state(self, state):
        self._state = state
        self._state.set_elevator(self)

    def show_state(self):
        print(f'Eleventor state is : {self._state.__class__.__name__}')

    def go_up(self):
        self._state.push_up_btn()

    def go_down(self):
        self._state.push_down_btn()


class Floor(abc.ABC):
    _elevator = None

    def set_elevator(self , elevator):
        self._elevator = elevator

    @abc.abstractclassmethod
    def push_down_btn(self):
        pass

    @abc.abstractclassmethod
    def push_up_btn(self):
        pass


class FirstFloor(Floor):

    def push_down_btn(self):
        print('Already in the bottom floor')

    
    def push_up_btn(self):
        print('Eleventor moving upward one floor')
        self._elevator.set_state(SecondFloor())


class SecondFloor(Floor):

    def push_down_btn(self):
        print('Eleventor moving down a floor')
        self._elevator.set_state(FirstFloor())

    def push_up_btn(self):
        print('Already in the bottom floor')


a = Elevator(FirstFloor())
a.show_state()
a.go_up()
a.show_state()
a.go_down()
a.show_state()