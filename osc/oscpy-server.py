from oscpy.server import OSCThreadServer
from time import sleep
import sys

def callback_message(*values):
    print(values)


def callback_bundle(*values):
    print("in bundle")
    print(values)

def main():
    ip = '0.0.0.0'

    osc = OSCThreadServer(encoding='utf8')
    # sock = osc.listen(address='192.168.1.85', port=5555, default=True)
    print("Listening on port 5555...")
    sock = osc.listen(address=ip, port=5555, default=True)

    osc.bind('/ping', callback_message)
    osc.bind(b'/pong', callback_bundle)
    sleep(1000)
    # osc.stop()

if __name__ == "__main__":
    main()
