import socket
from xml.dom import minidom
import threading
import fichier.var as var
import fichier.Snyf.fct as snyf_fct
import re


def send(type):
    if type == 'hik':
        msg = b'<?xml version="1.0" encoding="utf-8"?><Probe><Uuid>3CE54408-8D8E-4D4F-84E8-B6A50004400A</Uuid><Types' \
              b'>inquiry</Types></Probe> '
        port = 37020
    if type == 'avigilon':
        msg = b'<?xml version="1.0" encoding="UTF-8"?><s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:d="http://schemas.xmlsoap.org/ws/2005/4/discovery" xmlns:dn="http://www.onvif.org/ver10/network/wsdl" ><s:Header><a:Action s:mustUnderstand="1">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</a:Action><a:MessageID>:uuid:51807d09-8736-437e-9980-f3151c4ad948</a:MessageID><a:To s:mustUnderstand="1">urn:schemas-xmlsoap-org:ws:2005:04:discovery</a:To></s:Header><s:Body><Probe xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><d:Types>dn:NetworkVideoTransmitter</d:Types><MaxResults xmlns="http://schemas.microsoft.com/ws/2008/06/discovery">100</MaxResults><Duration xmlns="http://schemas.microsoft.com/ws/2008/06/discovery">PT1M</Duration></Probe></s:Body></s:Envelope>'
        port = 3702
    if type == 'onvif':
        msg = b'<?xml version="1.0" encoding="utf-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsd="http://schemas.xmlsoap.org/ws/2005/04/discovery" xmlns:dn="http://www.onvif.org/ver10/network/wsdl"><SOAP-ENV:Header><wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action><wsa:MessageID>urn:uuid:00C2BD26-0000-0000-0000-000000004321</wsa:MessageID><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To></SOAP-ENV:Header><SOAP-ENV:Body><wsd:Probe><wsd:Types>dn:NetworkVideoTransmitter</wsd:Types></wsd:Probe></SOAP-ENV:Body></SOAP-ENV:Envelope>'
        port = 3702
    if type == 'upnp':
        msg = ('M-SEARCH * HTTP/1.1\r\n' +
                'HOST: 239.255.255.250:1900\r\n' +
                'MAN: "ssdp:discover"\r\n' +
                'MX: 1\r\n' +
                'ST: ssdp:all\r\n' +
                '\r\n')
        port = 1900
    if type == 'samsung':
        msg = ('M-SEARCH * HTTP/1.1\r\n' \
            'HOST:255.255.255.255:1900\r\n' \
            'MAN:"ssdp:discover"\r\n' \
            'MX:1\r\n' \
            'ST: urn:dial-multiscreen-org:service:dial:1\r\n' \
            'USER-AGENT: microsoft Edge/103.0.1518.61 Windows\r\n' \
            '\r\n')
        port = 7701


    # Set up UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.settimeout(var.timeTest)

    def resp():
        try:
            i = 0
            while True:
                data, addr = s.recvfrom(port)
                ip = addr[0]
                donn = snyf_fct.pars(data.decode(), type)
                nom = donn[0]
                modele = donn[1]
                mac = donn[2]
                try:
                    var.q.put(lambda: var.tab_ip.insert(parent='', index=i, iid=ip, tag=ip, values=(ip, modele, mac, "", "", "")))
                    i += 1
                except:
                    print("error "+type)
                    pass
        except socket.timeout:
            pass


    def start():
        if type=="upnp":
            s.sendto(msg.encode(('ASCII')), ('239.255.255.250', port))
        else:
            s.sendto(msg, ('239.255.255.250', port))
        print("send "+type)
        t1 = threading.Thread(target=resp)
        t1.start()
    start()


