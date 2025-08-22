"""
    Facade
    - a structural design pattern that provides asimplified interface to a library,
    a framework or any other complex set of classes.
"""
#way 1 (Facade decide to use which subsystem)
class CPU: # Subsystem 1
    def execute(self):
        print('Executing')

class Memory: # Subsystem 2
    def load(self):
        print('Loading data.')        

class SSD: # Subsystem 3
    def read(self):
        print('read data from SSD')

class Computer: # Facade
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()
    def start(self):
        self.memory.load()
        self.ssd.read()
        self.cpu.execute()

def client_facade():
    computer_facade = Computer()
    computer_facade.start()

client_facade() 

#Way 2 (Client sends subsystem)
"""
    Facade - Way 2 (with *subsys)
    Client passes subsystems to the Facade
"""

# --- Subsystems ---
class CPU:  # Subsystem 1
    def execute(self):
        print("⚙️ CPU: Executing instructions")


class Memory:  # Subsystem 2
    def load(self):
        print("💾 Memory: Loading data")


class SSD:  # Subsystem 3
    def read(self):
        print("📀 SSD: Reading data")


# --- Facade ---
class Computer:
    def __init__(self, *subsys):
        # Store subsystems dynamically in a dict by class name
        self.subsystems = {sub.__class__.__name__: sub for sub in subsys}

    def start(self):
        # Use subsystems if they exist
        if "Memory" in self.subsystems:
            self.subsystems["Memory"].load()
        if "SSD" in self.subsystems:
            self.subsystems["SSD"].read()
        if "CPU" in self.subsystems:
            self.subsystems["CPU"].execute()


# --- Client ---
def client_facade():
    # Client decides which subsystems to use
    cpu = CPU()
    memory = Memory()
    ssd = SSD()

    # Pass any number of subsystems
    computer_facade = Computer(cpu, memory, ssd)
    computer_facade.start()

    print("\n--- Minimal subsystems ---")
    # Client can also build a lightweight computer
    minimal_computer = Computer(cpu, memory)  # no SSD
    minimal_computer.start()

    print(">>> Minimal Computer (CPU only)")
    computer_cpu_only = Computer(cpu)
    computer_cpu_only.start()

client_facade()    