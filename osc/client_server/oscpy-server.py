from oscpy.server import OSCThreadServer
from time import sleep

def callback(*values):
    print(values)

osc = OSCThreadServer()
sock = osc.listen(address='192.168.1.85', port=5555, default=True)
osc.bind(b'/ping', callback)
sleep(1000)
#osc.stop()
