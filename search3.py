#!/usrbin/python3
# Foundations of Python Network Programming., THird Edition

import socket
from urllib.parse import quote_plus

request_text ="""\
GET     /maps/api/geocode/json?address={} &sensor=false HTTP/1.1\r\n\
HOST:maps.google.com:80\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    sock = socket.socket()
    sock.connect(('maps.google.com',80))
    