from coapthon.client.helperclient import HelperClient

host = "192.168.1.8"
port = 5555
path ="basic"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()