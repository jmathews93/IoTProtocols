from coapthon.client.helperclient import HelperClient
import json, sys
from time import sleep

# Hard limit of 9203 for the substring/ character limit


if len(sys.argv) > 2:
    file_name = sys.argv[2]
    print("file name: ", file_name)
    file = open(file_name, "r")
    jsn = file.read()
    # print("file contents: ", json)

    with open(file_name) as f:
      data = json.load(f)

    loop_len = len(data['allTides'])

    # host = "192.168.1.5"
    host = sys.argv[1]
    port = 5555
    path = "basic"

    client = HelperClient(server=(host, port))
    # Hard limit of 9203 for the substring/ character limit b\c OSX



file_name = sys.argv[2]
file = open(file_name, "r")
jsn = file.read()

with open(file_name) as f:
  data = json.load(f)

loop_len = len(data['allTides'])

def test_case_1():
    global data, client, loop_len
    """
    Sends each recrord in the JSON file separately.
    """

    for i in range(loop_len):
        list = []
        list.append(data['allTides'][i]['time'])
        list.append(data['allTides'][i]['height'])
        client.post(path, list)



def test_case_2():
    global client, jsn
    """
    Sends the first 9203 characters (bytes) in the string representation
    of the json file.
    """

    for i in range(loop_len):
        client.put(path, jsn[0:9203])


def test_case_3():
    global osc, jsn
    """
    Sends the first 65000 characters in the string representation
    of the json file to simulate a max packet size.
    """

    for i in range(loop_len):
        client.post(path, jsn[0:65000])

def main():
    # print "Test Case 1:"
    # for i in range(100):
    #     print "Trial", i, "\n"
    #     test_case_1()
    #     print "End Trial", i, "\n"
    #     sleep(1)
    # sleep(15)
    test_case_1()
    # print "Test Case 2:"
    # for i in range(100):
    #     print "Trial", i, ":"
    #     test_case_2()
    #     print "End Trial", i, "\n"
    #     sleep(1)
    # sleep(15)

    # print "Test Case 3"
    # for i in range(100):
    #     print "Trial", i, ":"
    #     test_case_3()
    #     print "End Trial", i, "\n"
    #     sleep(1)

    client.stop()

if __name__ == "__main__":
    main()
