########################
# Networked Programs
########################

# -- Internet is built on top of TPC protocol and its layers
# -- we're going to ignore the low level layers and focus on TRANSPORT and APPLICATION layers
# -- TRANSPORT layer - assumes that there are two computers running two separate processes and
#       there is a pipe connecting both computers where we can talk and listen to.
# -- This endpoint of data phone call (connection) is called a socket.

# -- An internet socket is an endpoint of a bidirectional inter-process communication flow across an internet
#       protocol-based computer network, such as the Internet.
# --        PROCESS <-----> INTERNET <-----> PROCESS
#           (browser)                       (web server)

# -- TPC PORT NUMBERS - We need to decide which systems to talk to, and which services on these systems
#       Think of the ports as an organization phone number extension (RAMAL)
#   - Incoming e-mail (port 25)
#   - Insecure Login (port 23)
#   - Insecure web (port 80) ; Secure web (port 443)
#   - Personal Mail Box (port 109 / 110)

# -- Telnet (23) - Login                    IMAP (143/220/993) - Mail Retrieval
# -- SSH (22) - Secure Login                POP (109/110) - Mail Retrieval
# -- HTTP (80)                              DNS (53) - Domain Name
# -- HTTPS (443) - Secure                   FTP (21) - File Transfer
# -- SMTP (25) - Mail

# -- sometimes we see the port number in the URL if the web server is running on a non-standard port
#       ex: www.lasi-asia.org:8080/wp/

# in python, we can talk directly to sockets using socket module

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM says that is a series of characters that /
#                                                             comes one after another instead of blocks of text.
mysock.connect(('data.pr4e.org', 80))  # host and port
#                                        -- make the phone call to this host on that port

########################
# Application Protocols
########################
# -- what kind of data do we expect to send or to receive now that we have the socket?
# -- the application protocol is what handles this, after the "phone call" is made

# HTTP - Hypertext Transfer Protocol
# -- Invented for the web to retrieve HTML, Images, Documents, etc.
# -- A protocol is a set of rules that all parties follow so we can predict each other's behaviour.

# protocol/host/document -> https://www.dr-chuck.com/page1.htm

# GETTING DATA FROM THE SERVER
# -- Each time the user clicks to an anchor tag with a href= value to switch to a new page, the browser makes a
# connection to the web server and issues a GET request - to GET the content of the page at the specified URL, then
# the server returns the HTML document to the browser which formats and displays the document to the user.

# The Internet Standards are documents called RFCs created by an organization called IETF.


########################
# Write a Web Browser
########################

# HTTP Request in python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Corrected HTTP request structure with proper host and resource path
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()  # encode converts from Unicode to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512)  # ask for up to 512 char
    if len(data) < 1:
        break
    print(data.decode(), end='')  # decode converts from UTF-8 to Unicode

mysock.close()

# -- the output will contain metadata, a blank line and then the content
# -- the blank line means for the software developer that the header has ended and what comes next is the content.

########################
# Characters and Strings
########################

# ASCII
# -- each character is represented by a number between 0 and 256 stored in 8 bits of memory.
# -- we refer to 8 bits of memory as a byte
# -- ord() function used to get the numeric ASCII value

print(ord('H'))
print(ord('\n'))

# UNICODE
# -- Billions more characters than ASCII
# -- Sending Unicode via internet would be way too large (UTF-32)
# -- UTF-32 -> 4 bytes
# -- UTF-16 -> 2 bytes
# -- UTF-8 -> 1-4 bytes (dynamic length, so it is the best practice to move data over the internet)

# in python3 all strings are unicode
# when we talk to a network resource using sockets or talk to a database we have to encode and decode data (UTF-8)
# encode str to bytes (UTF-8) ;; decode bytes (UTF-8) to str

########################
# URLIB
########################



########################
# Code Example: urlib1.py, urlwords.py
########################


########################
# Parsing HTML
########################


########################
# Code Example: urlinks.py
########################
