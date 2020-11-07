from pythonosc.udp_client import SimpleUDPClient
import sys

from oscpy.server import OSCThreadServer
from time import sleep

def callback(values):
    print("got values: {}".format(values))




file = open("../../tides.json", "r")
json = file.read()

if __name__ == "__main__":

    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print("IP: ", ip)
        port = 5555

        osc = OSCThreadServer()
        sock = osc.listen(address=ip, port=port, default=True)
        osc.bind(b'/address', callback)
        sleep(1000)
        #osc.stop()


        # 
        # client = SimpleUDPClient(ip, port)  # Create client
        #
        # client.send_message("/some/address", 123)   # Send float message
        # client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
