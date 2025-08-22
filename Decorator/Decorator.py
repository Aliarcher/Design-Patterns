"""
    Decorator
    - a structural pattern that allows adding new behaviors to objects dynamically
    by placing them inside special wrapper objects,called decorators.
"""
import abc
#way 1 (GoF structural pattern style.)
import abc

# --- Abstract Component ---
class Page(abc.ABC):
    @abc.abstractmethod
    def show(self):
        pass


# --- Concrete Components ---
class AuthPage(Page):
    def show(self):
        print("✅ Welcome to authenticated page")


class AnonPage(Page):  # fixed typo: AnnonPage → AnonPage
    def show(self):
        print("👤 Welcome to anonymous page")


# --- Abstract Decorator ---
class PageDecorator(Page, abc.ABC):
    def __init__(self, component: Page):
        self._component = component

    @abc.abstractmethod
    def show(self):
        pass


# --- Concrete Decorator ---
class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password == "secret":
            self._component.show()
        else:
            print("❌ You are not authenticated")
            anon_page = AnonPage()
            anon_page.show()


# --- Client ---
def client_decorator():
    page = AuthPage()
    decorated_page = PageAuthDecorator(page)  # wrap it with decorator
    decorated_page.show()



client_decorator()

#way2 (Pythonic @decorator style.)
from functools import wraps

# --- Abstract Component (base function as "Page") ---
def anon_page():
    print("👤 Welcome to anonymous page")


def auth_page():
    print("✅ Welcome to authenticated page")


# --- Decorator ---
def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password == "secret":
            return func(*args, **kwargs)
        else:
            print("❌ You are not authenticated")
            anon_page()
    return wrapper


# --- Concrete Component with annotation ---
@auth_required
def show_page():
    auth_page()


# --- Client ---
if __name__ == "__main__":
    #Way1
    client_decorator()
    #Way2
    show_page()    