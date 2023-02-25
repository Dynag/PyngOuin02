#!/usr/bin/env python2
import socket  
import sys
import re
import sys
import time
import base64
import struct
import socket
import xml.etree.ElementTree as ET
import base64
dst = "239.255.255.250"  
if len(sys.argv) > 1:  
    dst = sys.argv[1]
st = "upnp:rootdevice"  
if len(sys.argv) > 2:  
    st = sys.argv[2]
msg = ('M-SEARCH * HTTP/1.1\r\n' +
                    'HOST: 239.255.255.250:1900\r\n' +
                    'MAN: "ssdp:discover"\r\n' +
                    'MX: 1\r\n' +
                    'ST: ssdp:all\r\n' +
                    '\r\n')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  
s.settimeout(10)  
s.sendto(msg.encode(('ASCII')), (dst, 1900))
while True:  
    try:
        data, addr = s.recvfrom(32*1024)
    except socket.timeout:
        break
    print("[+] %s\n%s" % (addr, data))