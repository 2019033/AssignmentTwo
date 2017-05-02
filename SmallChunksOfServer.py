import socket
IP = "10.10.18.223"
port = 30000
buffer = 1024
applicationName = "Project Mercury"
	
class Server():
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((IP,port))
		self.s.listen(5)
		self.conn, self.addr = self.s.accept()
		print("Connection has been made.")
		self.waitForLogin()



	def waitForLogin(self):
		self.loginstuff = self.conn.recv(buffer).decode('utf-8')
		if self.loginstuff[0] == "#":
			self.createNewLogin()
		else:
			self.verifyLogin()

	def verifyLogin(self):
		for i in range(0,len(self.loginstuff),1):
			if self.loginstuff[i] == "$":
				self.atpoint = i
		self.username = self.loginstuff[1:self.atpoint]
		self.password = self.loginstuff[self.atpoint+1:]

			with open("accounts.txt") as openfile
				for line in openfile:
					if 


	def createNewLogin(self):
		print("Not done")
	


Server().__init__()