from oscpy.client import OSCClient
import json, sys
from time import sleep

# Hard limit of 9203 for the substring/ character limit

num_tests = 30

if len(sys.argv) > 1:
    ip = sys.argv[1]
    print("IP: ", ip)
    port = 5555

file_name = sys.argv[2]
file = open(file_name, "r")
jsn = file.read()
osc = OSCClient(ip, port, encoding='utf8')

with open(file_name) as f:
  data = json.load(f)

loop_len = len(data['allTides'])

def test_case_1():
    global data, osc
    """
    Sends each recrord in the JSON file separately.
    """

    for i in range(10000):
        list = []
        list.append(data['allTides'][i]['time'])
        list.append(data['allTides'][i]['height'])
        osc.send_message('/ping', list)



def test_case_2():
    global osc, jsn
    """
    Sends the first 9203 characters in the string representation
    of the json file.
    """
    for i in range(10000):
        osc.send_message('/ping', [jsn[0:9203]], safer=True)


def test_case_3():
    global osc, jsn
    """
    Sends the first 65000 characters in the string representation
    of the json file to simulate a max packet size.
    """
    for i in range(10000):
        osc.send_message('/ping', [jsn[0:65000]], safer=True)

def main():
    osc.send_message('/ping', [1], safer=True)
    sleep(1)


    # print "Test Case 1:"
    # for i in range(num_tests):
    #     print "Trial", i, "\n"
    #     test_case_1()
    #     print "End Trial", i, "\n"
    #     sleep(0.2)

    print "Test Case 2:"
    for i in range(num_tests):
        print "Trial", i, ":"
        test_case_2()
        print "End Trial", i, "\n"
        sleep(0.2)
    # #
    # print "Test Case 3"
    # for i in range(num_tests):
    #     print "Trial", i, ":"
    #     test_case_3()
    #     print "End Trial", i, "\n"
    #     sleep(0.2)

    
    osc.send_message('/ping', [1], safer=True)

if __name__ == "__main__":
    main()
