from coapthon.client.helperclient import HelperClient

import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print("file name: ", file_name)
        file = open(file_name, "r")
        json = file.read()
        print("file contents: ", json)

        host = "192.168.1.8"
        port = 5555
        path = "basic"

        client = HelperClient(server=(host, port))
        response = client.get(path)
        print(response.pretty_print())
        client.stop()
