#!/bin/bash

PIP_VER=$(pip --version)
PIP3_VER=$(pip3 --version)
PY_VER="${PIP_VER: -12}"
PY_VER3="${PIP3_VER: -12}"

echo "${PY_VER:1:8}"
echo "${PY_VER3:1:8}"

if [ "${PY_VER:1:8}" = "python 3" ] 
then
    echo "PIP"
    pip install paho-mqtt
    sudo pip install CoAPthon
    pip install python-osc
elif [ "${PY_VER3:1:8}" = "python 3" ]
then
    echo "PIP3"
    pip3 install paho-mqtt
    sudo pip3 install CoAPthon
    pip3 install python-osc
fi
    

