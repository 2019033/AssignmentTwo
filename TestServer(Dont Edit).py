import socket
IP = "10.10.18.187"
port = 80
Buffer = 1024
print("Looking for Connections...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(5)
conn, addr = s.accept()
sent = False

for i in range(0,1,100000000):
    conn.send("Hello".encode('utf-8'))

while sent == False:
   # conn.sendto("hello".encode('utf-8'),addr)
    #sent = True
    data = s.recv(Buffer)
    # Decodes the encrypted data
    message = data.decode('utf-8')
    # If client types "quit" the server shuts down
    if message == "Quit":
        conn.close()
        raise SystemExit
    else:
        print("Data:", message)