from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

import sys

def print_handler(address, *args):
    print("{address}: {args}")


def default_handler(address, *args):
    print("DEFAULT {address}: {args}")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        port = 5555

        dispatcher = Dispatcher()
        dispatcher.map("/something/*", print_handler)
        dispatcher.set_default_handler(default_handler)


        print("Listening on port 5555...")

        server = BlockingOSCUDPServer((ip, port), dispatcher)
        server.serve_forever()  # Blocks forever
