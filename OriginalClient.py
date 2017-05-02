#Import statements
import socket
# Setup Variables
Message = 'h'
#IP & Port the client is connecting to
IP = '10.10.18.234'
Port = 443
Buffer = 1024

#Makes the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP,Port))

#Allows user to send unlimited messages to the server
while Message != '':
    Message = input("enter text: ")
    s.send(Message.encode('utf-8'))
