from pythonosc.udp_client import SimpleUDPClient
import sys

# file = open("../../tides.json", "r")
# json = file.read()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print("IP: ", ip)
        port = 5555

        file_name = sys.argv[2]
        print(file_name)
        file = open(file_name, "r")
        json = file.read()
        print(json)

        client = SimpleUDPClient(ip, port)  # Create client

        client.send_message("/some/address", json)   # Send float message
        # client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
