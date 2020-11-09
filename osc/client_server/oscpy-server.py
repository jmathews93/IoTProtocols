from oscpy.server import OSCThreadServer
from time import sleep

def callback(values):
    print("got values: {}".format(values))

osc = OSCThreadServer()
sock = osc.listen(address='172.25.27.69', port=5555, default=True)
osc.bind(b'/ping', callback)
sleep(1000)
#osc.stop()

#from oscpy.server import OSCThreadServer
