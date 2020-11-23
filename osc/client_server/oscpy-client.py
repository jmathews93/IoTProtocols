from oscpy.client import OSCClient
import json, sys

osc = OSCClient("192.168.1.85", 5555, encoding='utf8')   # JA
osc = OSCClient("73.131.93.124", 5555, encoding='utf8')  # Jared


file = open('../../tides.json', 'r')
x = file.read()
print(sys.getsizeof(x))

with open('../../tides.json') as f:
  data = json.load(f)


for i in range(len(data['allTides'])):
    list = []
    list.append(data['allTides'][i]['time'])
    list.append(data['allTides'][i]['height'])
    osc.send_message(b'/ping', list)
