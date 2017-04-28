#Import Statements
from tkinter import * #Tkinter for GUI
import socket #Sockets used for networking aspect of assignment
import time
import base64
import _thread
import os
# Setup Variables
programName = "Project Mercury"

#Target location of connection
host = '10.10.18.223'
port = 30000
buffer = 1024
#The main Client class
class Client():
    #Init function, ran on start up
    def __init__(self):
        try:
            #Attempts to connect to server and opens login window

            self.connect()
            self.loginScreen()
            print('Waiting for server...')
            #Error window if cannot connect to server
        except ConnectionRefusedError:

            #Creates error window
            self.error = Tk()

            #Error window setups
            self.error.geometry("300x100")
            self.error.title(programName)

            #Error label
            self.errorMessage = Label(self.error,text = "Could not connect to server\n Please try again later.",font = ('Helvetica', 14))
            self.errorMessage.pack()

            #Error window loop
            self.error.mainloop()
            exit()
        #Login screen that first asks user if they are new or returning
    def loginScreen(self):
        if os.path.isfile("loginInfo.txt") == False:

            #Creates window
            self.screenA = Tk()
            
            #Setup variables
            self.screenA.geometry("250x200")
            self.screenA.title(programName)

            #Label
            self.account = Label(self.screenA,text = "Do you have an account already?")
            self.account.pack(side = TOP)


            #Yes and No buttons
            self.loginOption = Button(self.screenA,text = "Yes", command = self.login)
            self.loginOption.pack(side = BOTTOM, pady = 3)

            self.newOption = Button(self.screenA,text = "No",command = self.newAccount)
            self.newOption.pack(side = BOTTOM, pady = 3)

            #Window loop
            self.screenA.mainloop()
            exit()
            #self.screenA.destroy()
        else:
            self.useLoginInfo()


    def login(self):

        #Creates the login screen for usernames and password input
        self.screenB = Tk()
        self.screenA.destroy()

        #Usual setup variables
        self.screenB.geometry("250x200")
        self.screenB.title(programName)

        #Intro Label
        self.credentials = Label(self.screenB,text = "Enter your username and password")
        self.credentials.pack(side = TOP,pady = 10)

        #Username Information
        self.usernameLabel = Label(self.screenB,text = "Username:")
        self.usernameLabel.pack(side = TOP, pady= 3)
        self.usernameEntry = Entry(self.screenB)
        self.usernameEntry.pack(side = TOP, pady = 3)

        # Password Information
        self.passwordLabel = Label(self.screenB,text = "Password:")
        self.passwordLabel.pack(side = TOP, pady= 3,)
        self.passwordEntry = Entry(self.screenB,show = '*')
        self.passwordEntry.pack(side = TOP, pady = 3)

        # Login Button
        self.loginButton = Button(self.screenB,text = "Login",command = self.sendinfo)
        self.loginButton.pack(side = TOP,pady = 3)

        #Window loop
        self.screenB.mainloop()
        exit()
    def newAccount(self):
        #Creates the window
        self.screenC = Tk()
        self.screenA.destroy()

        #Screen settings
        self.screenC.geometry("300x400")
        self.screenC.title(programName)

        #Top Label
        self.creationLabel = Label(self.screenC,text = "Complete the fields below to create an account")
        self.creationLabel.pack(side = TOP,pady = 5)

        #Username Creation
        self.usernameCreation = Label(self.screenC,text = "Enter your username:")
        self.usernameCreation.pack(side = TOP,pady = 5)

        self.usernameCreationEntry = Entry(self.screenC)
        self.usernameCreationEntry.pack(side = TOP, pady = 3)

        # Email Creation
        self.email = Label(self.screenC,text = "Enter your email: ")
        self.email.pack(side = TOP, pady = 3)

        self.email = Entry(self.screenC)
        self.email.pack(side = TOP,pady = 3)


        # Password Creation
        self.passwordCreation = Label(self.screenC,text = "Enter your password: ")
        self.passwordCreation.pack(side = TOP, pady = 3)

        self.passwordCreationEntry = Entry(self.screenC)
        self.passwordCreationEntry.pack(side = TOP,pady = 3)

        #Re-enter password
        self.repassword = Label(self.screenC, text = "Re-enter your password: ")
        self.repassword.pack(side = TOP,pady = 3)

        self.repasswordEntry = Entry(self.screenC)
        self.repasswordEntry.pack(side = TOP, pady = 3)

        # Create Button
        signup = Button(self.screenC,text = "Create",command = self.getCreation)
        signup.pack(side = TOP,pady = 3)

        #Window Loop
        self.screenC.mainloop()
        exit()

    def getCreation(self):
        username = self.usernameCreationEntry.get()
        password = self.passwordCreationEntry.get()
        email = self.email.get()
        repassword = self.repasswordEntry.get()

        # If re-entering the password does not match the the original password
        if password != repassword:
            #Creates error window
            self.passwordMatch = Tk()
            #Setup variables
            self.passwordMatch.geometry("300x200")
            self.passwordMatch.title(programName)

            # Error label
            self.match = Label(self.passwordMatch,text = "Passwords do not match")
            self.match.pack(side = TOP)

            #Window loop
            self.passwordMatch.mainloop()
            time.sleep(2)

        # Checks if any of the fields have been left blank
        if username == "" or password == "" or email == "":

            # Creates error window
            self.usernameMatch = Tk()

            # Setup variables
            self.usernameMatch.geometry("300x200")
            self.usernameMatch.title(programName)

            # Error label
            self.match = Label(self.usernameMatch, text="One of the fields has been left empty")
            self.match.pack(side=TOP)

            # Window loop
            self.usernameMatch.mainloop()

        #Prepares to send the information to the server, where it will go through a checking process

        self.finalUsername = '#'+username
        self.finalPassword = '|'+password
        self.finalEmail = ">"+email
        self.finalCreation = self.finalUsername + self.finalPassword + self.finalEmail

        self.server.send(self.finalCreation.encode('utf-8'))
        self.saveInfor()


    #Function the begins connection with the server

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))
      #  self.server.listen(5)
       # self.conn = self.server.accept()

       # client = self.server.accept()

    def sendinfo(self):
        self.username = "@"+self.usernameEntry.get()
        self.password = "$"+self.passwordEntry.get()
        self.tosend = self.username + self.password
        self.server.send(self.tosend.encode('utf-8'))


#def loadingMessages(self):

 #   for i in range(0,1,100000):
   #     data = self.server.recv(buffer)
  #      print(data.decode())

    def saveInfor(self):
        # Checks if file exists
        if os.path.isfile("loginInfo.txt") == False:
            
            #Creates the window
            self.save = Tk()

            # Setup vairables
            self.save.geometry("300x300")
            self.save.title(programName)

            #Buttons and Labels   
            Label1 = Label(self.save,text = "Would you like to save your login information for later?")
            Label1.pack(side = TOP, pady = 3)
            save = Button(self.save,text = "Yes",command = self.saveToFile)
            save.pack(side = TOP,pady= 3)
            dontSave = Button(self.save,text = "No",command = self.chatWindow)
            dontSave.pack(side = TOP,pady = 3)
        else: 
            self.useLoginInfo()

        self.save.mainloop()

    def saveToFile(self):
      #Creates Login file
       saveLogin = open("loginInfo.txt","a")
       
    #Writes login data to file
       saveLogin.write(self.username + "\n" + self.password + "\n" + self.email)

    def useLoginInfo():
        # Not implemented as of yet.
        savedInf = open("loginInfo.txt","a")


# Events that occur when a message is sent and when a message is being loaded

    """These two functions essentially update the message box when a new message comes in, it
    updates the message box when a user sends a message, prevents the user from being able to type in the 
    message box.  """
    def PressAction(event, self):
        self.EntryBox.config(state=NORMAL)
        ClickAction()

    def DisableEntry(event, self):
        self.EntryBox.config(state=DISABLED)

    #Functions that takes messages and sends them to server. 
    def ClickAction(self):
        #Write message to chat window
        self.EntryText = FilteredMessage(self.EntryBox.get("0.0",END))
        LoadMyEntry(self.ChatLog, self.EntryText)

        #Scroll to the bottom of chat windows
        self.ChatLog.yview(END)

        #Erase previous message in Entry Box
        self.EntryBox.delete("0.0",END)
            
        #Send my mesage to all others
        self.server.send(EntryText.encode('utf-8'))


    def chatWindow(self):
        
        # Creates the window
        self.Window = Tk()
        
        # Window and size
        self.Window.geometry("400x500")
        self.Window.title(programName)


        #Chat Log
        self.ChatLog = Text(self.Window, bd=0, bg="white", height="8", width="50", font="Arial",)
        self.ChatLog.insert(END, "Connecting to your partner..\n")
        self.ChatLog.config(state=DISABLED)
        
        #Scroll Bar
        self.scrollbar = Scrollbar(self.Window, command=ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = self.scrollbar.set

        #Send 
        self.SendButton = Button(self.Window, font=30, text="Send", width="12", height=5,
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command=ClickAction)

        #Entry Box where messages are typed
        self.EntryBox = Text(self.Window, bd=0, bg="white",width="29", height="5", font="Arial")
        self.EntryBox.bind("<Return>", DisableEntry)
        self.EntryBox.bind("<KeyRelease-Return>", PressAction)

        #Placing on screen
        self.scrollbar.place(x=376,y=6, height=386)
        self.ChatLog.place(x=6,y=6, height=386, width=370)
        self.EntryBox.place(x=128, y=401, height=90, width=265)
        self.SendButton.place(x=6, y=401, height=90)


        #Window loop
        self.Window.mainloop()

Client().__init__()
#_thread.start_new_thread(Client, args)
