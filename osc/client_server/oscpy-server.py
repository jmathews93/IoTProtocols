from oscpy.server import OSCThreadServer
from time import sleep

def callback_message(*values):
    print(values)

def callback_bundle(*values):
    print("in bundle")
    print(values)

osc = OSCThreadServer(encoding='utf8')
sock = osc.listen(address='192.168.1.85', port=5555, default=True)
osc.bind('/ping', callback_message)
osc.bind(b'/pong', callback_bundle)
sleep(1000)
#osc.stop()
