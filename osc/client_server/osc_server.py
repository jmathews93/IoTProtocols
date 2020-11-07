from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


def print_handler(address, *args):
    print("{address}: {args}")


def default_handler(address, *args):
    print("DEFAULT {address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/something/*", print_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1" #localhost
port = 5555

print("Listening on port 5555...")

server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever

