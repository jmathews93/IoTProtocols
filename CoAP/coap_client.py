from coapthon.client.helperclient import HelperClient

import sys

def main():
    if len(sys.argv) > 2:
        file_name = sys.argv[2]
        print("file name: ", file_name)
        file = open(file_name, "r")
        file_payload = file.read()
        # print("file contents: ", json)

        # host = "192.168.1.5"
        host = sys.argv[1]
        port = 5555
        path = "basic"

        client = HelperClient(server=(host, port))
        # Hard limit of 9203 for the substring/ character limit b\c OSX
        response = client.put(path, file_payload[0:9203])
        print(response.pretty_print())
        client.stop()

if __name__ == "__main__":
    main()
