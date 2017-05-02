#Import statements
import socket
import _thread
import usernamePasswordDirectory


#Setup Variables
IP = "10.10.18.223"
port = 30000
Buffer = 1024
applicationName= "Assignment 2"
connection= False
passwordVer= False
clientErrorMessage=""
global username
username= ""
global password
password= ""
sucessfulLogin= False


#Beginning search for clients
print("Looking for Connections...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(5)
conn, addr = s.accept()
connection=True


#this function will authenticate the username and password of the user
def passwordVerification():

    #waiting for the password to be sent
    while True:
        # waiting for the client to send the username and password
        jumble = conn.recv(Buffer)
        
        #seperating the variable sent by the client into a username and a password variable
        
        jumble=str(jumble)
        newJumble=jumble[3:len(jumble)]
        
        for i in range(0,len(newJumble),1):
            #the $ sign means that it is the password. Therefore whatever is before it is the username
            if newJumble[i]=='$':
                username=newJumble[0:i-1]
                password=newJumble[i:len(newJumble-1)]
               
        print (username)
        print (password)
        #finding the special username and password signs and using them to 

        #checking if the string sent by the client starts with '@'. The client attaches an '@' sign to all usernames and
        #password
        if username[0]!="@":
            clientErrorMessage=="notExpectedUsername"

            #sending an error message to the client letting them know why they have been denied access to the chat systems
            conn.send(clientErrorMessage.encode('utf-8'))
            pass

        #checking if a password has been sent by seeing if it has the '@' sign
        if password[0]!='@':
            clientErrorMessage == "notExpectedPassword"

            # sending an error message to the client letting them know why they have been denied access to the chat systems
            conn.send(clientErrorMessage.encode('utf-8'))
            pass

        if username[0]=='@' and password[0]== '@':
            # if both a username and a password has been sent to the server than it will continue with the verification process
            #this will break out of the while loop
            break


        #this is for debugging purposes

        print("The user who is trying to connect:",username)
        print("The password they have entered:",password)


        #we will now call up our username and password dictionairy to verify the users credidentials

        #first, we are checking if the username that the client entered is even in our database

        if username in usernamePasswordDirectory.userPassList:
            #if the username is in the directory, then we retrieve the actual user's real password and we compare it to
            #the password provided by the client
            realPassword = usernamePasswordDirectory.userPassList[username]

            #if the password is correct, then a message is said to the client and the user is allowed to start sending messages
            if password==realPassword:
                sucessfulLogin=True
                clientSuccessMessage=('passwordVerSucessful')
                conn.send(clientSuccessMessage.encode('utf-8'))

                #calling the main menu function
                main()


            #if the password is incorrect, then the login process starts again
            else:
                clientErrorMessage == "notCorrectPassword"

                # sending an error message to the client letting them know why they have been denied access to the chat systems
                conn.send(clientErrorMessage.encode('utf-8'))

        #if the username isnt even in the directory, then the server lets the client know
        else:
            clientErrorMessage == "notExpectedUsername"

            # sending an error message to the client letting them know why they have been denied access to the chat systems
            conn.send(clientErrorMessage.encode('utf-8'))

            #restarting the password verification function so that the user will be allowed to re-enter their credidentials
            passwordVerification()


#this function triggers the main menu where the user will be allowed to do a variety of actions
def main():
    None





#Function for receiving messages from client
def Messages(Buffer):
    #Prints the connecting address, of the client
    print("Connection Address: ",addr)
    while True:
        data = conn.recv(Buffer)
        #Decodes the encrypted data
        message = data.decode('utf-8')
        #If client types "quit" the server shuts down
        if message == "Quit":
            conn.close()
            raise SystemExit
        else:
            print("Data:", message)

        data = input(">>>")
        c.send(data.encode('utf-8'))

#Introduction to threading, still learning about this
_thread.start_new_thread(Messages ,(Buffer, ))

#Runs the program
while 1:
    pass


