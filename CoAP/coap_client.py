from coapthon.client.helperclient import HelperClient

import sys

if __name__ == "__main__":

    if len(sys.argv) > 2:
        file_name = sys.argv[1]
        print("file name: ", file_name)
        file = open(file_name, "r")
        json = file.read()
        ip = sys.argv[2]
        print("IP: ", str(ip))
        # print("file contents: ", json)

        # host = "192.168.1.5"
        host = sys.argv[2]
        port = 5555
        path = "basic"

        client = HelperClient(server=(host, port))
        response = client.put(path, "hello")
        print(response.pretty_print())
        client.stop()
