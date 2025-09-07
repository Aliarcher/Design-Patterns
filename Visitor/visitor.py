import abc

class PublicVehicle(abc.ABC):

    def __init__(self , dest):
        self.dest = dest

    @abc.abstractclassmethod
    def order_ticket(self, ordering):
        pass


class Train(PublicVehicle):

    def order_ticket(self, ordering):
        ordering.train_ticket(self)


class Bus(PublicVehicle):

    def order_ticket(self, ordering):
        ordering.bus_ticket(self)


class Plane(PublicVehicle):

    def order_ticket(self, ordering):
        ordering.plane_ticket(self)


class Ticket(abc.ABC):

    @abc.abstractclassmethod
    def train_ticket(self, train):
        pass

    @abc.abstractclassmethod
    def bus_ticket(self, bus):
        pass

    @abc.abstractclassmethod
    def plane_ticket(self, plane):
        pass


class Order(Ticket):


    def train_ticket(self, train):
        print(f'This is a train ticket to: {train.dest}')


    def bus_ticket(self, bus):
        print(f'This is a bus ticket to: {bus.dest}')

    def plane_ticket(self, plane):
        print(f'This is a plane ticket to: {plane.dest}')

o = Order()
Plane('Shiraz').order_ticket(o)
