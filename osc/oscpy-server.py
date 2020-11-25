from oscpy.server import OSCThreadServer
from time import sleep
import sys

def callback_message(*values):
    print(values)


def callback_bundle(*values):
    print("in bundle")
    print(values)


if __name__ == "__main__":
    if len(sys.argv) > 0:
        ip = sys.argv[1]
        print("IP: ", ip)

        osc = OSCThreadServer(encoding='utf8')
        # sock = osc.listen(address='192.168.1.85', port=5555, default=True)
        sock = osc.listen(address=ip, port=5555, default=True)

        osc.bind('/ping', callback_message)
        osc.bind(b'/pong', callback_bundle)
        sleep(1000)
        # osc.stop()
