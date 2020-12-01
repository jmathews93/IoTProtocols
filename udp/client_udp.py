import socket
import json, sys
from time import sleep


# Hard limit of 9203 for the substring/ character limit

if len(sys.argv) > 1:
    ip = sys.argv[1]
    print("IP: ", ip)
    port = 5555

    # msgFromClient       = "Hello UDP Server"
    serverAddressPort   = (ip, port)
    bufferSize          = 2048


    file_name = sys.argv[2]
    file = open(file_name, "r")
    jsn = file.read()

    with open(file_name) as f:
      data = json.load(f)

    loop_len = len(data['allTides'])

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    # UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    #msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    #msg = "Message from Server {}".format(msgFromServer[0])



def test_case_1():
    global data, UDPClientSocket
    """
    Sends each recrord in the JSON file separately.
    """

    for i in range(10000):
        list = []
        list.append(data['allTides'][i]['time'])
        list.append(data['allTides'][i]['height'])
        bytesToSend         = str.encode(str(list))
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)



def test_case_2():
    global UDPClientSocket, jsn
    """
    Sends the first 9203 characters in the string representation
    of the json file.
    """
    for i in range(10000):
        bytesToSend         = str.encode(jsn[0:9203])
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

def test_case_3():
    global UDPClientSocket, jsn
    """
    Sends the first 65000 characters in the string representation
    of the json file to simulate a max packet size.
    """
    for i in range(10000):
        bytesToSend         = str.encode(jsn[0:65000])
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

def main():
    testbytes = str.encode("1")
    UDPClientSocket.sendto(testbytes, serverAddressPort)
    sleep(1)


    print "Test Case 1:"
    for i in range(30):
        print "Trial", i, "\n"
        test_case_1()
        print "End Trial", i, "\n"
        sleep(0.2)

    # print "Test Case 2:"
    # for i in range(30):
    #     print "Trial", i, ":"
    #     test_case_2()
    #     print "End Trial", i, "\n"
    #     sleep(0.2)
    # #
    # print "Test Case 3"
    # for i in range(30):
    #     print "Trial", i, ":"
    #     test_case_3()
    #     print "End Trial", i, "\n"
    #     sleep(0.2)


    UDPClientSocket.sendto(testbytes, serverAddressPort)


if __name__ == "__main__":
    main()
