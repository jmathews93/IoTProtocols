from oscpy.client import OSCClient
import json, sys

# Hard limit of 9203 for the substring/ character limit

osc = OSCClient("192.168.1.85", 5555, encoding='utf8')   # JA
#osc = OSCClient("73.131.93.124", 5555, encoding='utf8')  # Jared

file = open('../../tides.json', 'r')
x = file.read()
str = "x"*65000   ### generates a string taking up 65049 bytes in memory

with open('../../tides.json') as f:
  data = json.load(f)

### debug ###
print("size of text file", sys.getsizeof(x))
print("size of x*65000", sys.getsizeof(str))
print("size of x[0:9203]", sys.getsizeof(x[0:9203]))
### debug ###

osc.send_message('/ping', [bytes(x[0:9203], 'utf-8')], safer=True)

### this will only work if you have run the following command:
###     sudo sysctl -w net.inet.udp.maxdgram=65535
#osc.send_message('/ping', [x[0:65000]], safer=True)

for i in range(len(data['allTides'])):
    list = []
    list.append(data['allTides'][i]['time'])
    list.append(data['allTides'][i]['height'])
    osc.send_message(b'/ping', list)
