import abc

class Top(abc.ABC):
    """
    abstract class
    """

    def template_method(self):
        """
        This method should not be overridden.
        """
        self.first_method()
        self.second_method()
        self.third_method()
        self.fourth_method()

    def first_method(self):
        print('This is first method')

    def second_method(self):
        print('This is second method')


    @abc.abstractclassmethod
    def third_method(self):
        pass # must override method in child class

    @abc.abstractclassmethod
    def fourth_method(self):
        pass # must override method in child class



class One(Top):

    """
    creating class for first example
    """

    def third_method(self):
        print('This is third method from One class')


    def fourth_method(self):
        print('This is fourth method from One class')


class Two(Top):

    """
    creating class for second example
    """

    def third_method(self):
        print('This is third method from Two class')


    def fourth_method(self):
        print('This is fourth method from Two class')


def client(klass):
    klass.template_method()

client(Two())
