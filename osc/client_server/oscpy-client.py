from oscpy.client import OSCClient

osc = OSCClient("172.25.27.69", 5555)
for i in range(10):
    osc.send_message(b'/ping', [i])
