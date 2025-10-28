#!/usr/bin/python

from compiler.lang.rebeca.VirtualMachine import VirtualMachine
from compiler.lang.objects.Port import Interface

# Example implementation of a Port Interface to the eternal system,
# for example, a simulation environment or an real physical system.
# Here we define a simple port that just prints messages to the console
class PortExampleInterface(Interface):
    def __init__(self):
        super().__init__()

    def send(self, fd, msg, options=None):
        print(f"Sending message on port[{fd}]: {msg}")

    def receive(self, fd, options=None):
        print(f"Receiving message on port[{fd}]")
        return "Message received"

    def is_pending(self, fd):
        return False

    def is_open(self, fd):
        return True

    def setopt(self, fd, option, value):
        print(f"Setting option {option} to {value}")
        return True

    def getopt(self, fd, option):
        print(f"Getting option {option}")
        return None

    def connect(self, fd, address:str):
        print(f"Connecting to {address}")
        return True

    def open(self, type:str):
        print(f"Opening port of type {type}")
        return 19       # Example file descriptor

    def close(self, fd):
        print(f"Closing port {fd}")
        return True
    
if __name__ == '__main__':
    # Example usage of the Port with the Virtual Machine
    vm = VirtualMachine( {
        'port': PortExampleInterface()
        } 
    );

    # Load a Rebeca program that uses the port
    vm.load('ship.rebeca')

    # Start the simulation and run for a number of steps
    vm.start( {'ship': 'ship1'} )
    vm.step(numsteps=100)
    vm.stop()
