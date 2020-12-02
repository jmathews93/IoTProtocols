This project using python version 2.7.13.

Be sure to install pyenv and virtual env.

https://realpython.com/intro-to-pyenv/

OSC
----

python osc/oscpy-server.py

python osc/coscpy-client.py [IP_ADDRESS] [File To Send]


CoAP
----

python CoAP/coap_server.py

python CoAP/coap_client.py [IP_ADDRESS] [File To Send]


UDP
---

python udp/server_udp.py

python udp/client_udp.py [IP_ADDRESS] [File To Send]

All graphs are located in graphs/generated_graphs folder.
graphs/generated_graphs_old are deprecated
Charts in graphs/line_charts are quite gross so cleaner versions of them are in graphs/cleaner

Graphs can all be regenerated with graphs/generate_graphs.py though beware, it's very ugly and will require some prior knowledge on matplotlib. Each graph should be generated sepeartely for now until I can get in and clean it all up to make them all run in one go.
