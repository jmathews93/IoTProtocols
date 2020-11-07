from pythonosc.udp_client import SimpleUDPClient
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print("IP: ", ip)
        port = 5555

        client = SimpleUDPClient(ip, port)  # Create client

        client.send_message("/some/address", 123)   # Send float message
        client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
