from getpass import getpass
import random


# def myprint(self):
#     outputs.append(self)

# myprint('banana')

# myprint('banana again')
# open("output.txt", "w").write("\n".join(outputs))
# with open('output.txt','r') as file:
#      for line in file:
#         for word in line.split():
#             print(word) 

# password = getpass(prompt="Password: 🔒 ")

# print(password)

#user name, password, 
f = open("output.txt", "w")
class Bank:
    def __init__(self,initput):
        self.input = initput
    def createAccount(self):
        if self.input == "Create account".upper():
            self.name = input("Create an account name: ")
            self.number = random.randint(100000000000,999999999999)
            self.password = getpass(prompt="Password: 🔒 ")
            self.cPassword = getpass(prompt="Conform your Password: 🔒 ")
            while self.password != self.cPassword:
                print("Your type the wrong password, please type in again. ")
                self.password = getpass(prompt="Password: 🔒 ")
                self.cPassword = getpass(prompt="Conform your Password: 🔒 ")
            self.email = input("Please type in your email address: ")
            while (self.email[-4:] != ".com") or (self.email.find("@") == 0) or (len(self.email)<7):
                self.email = input("Please type in the correct email address: ")
            self.phone = input("Please type in your phone number: ")
            while len(self.phone) != 10:
                self.phone = input("Please type in the correct phone number: ")
            f = open("output.txt", "a")
            self.array = [self.name,str(self.number),self.password,self.email,self.phone]
            for self.bb in self.array:
                f.write(self.bb)
            f.write("\n")
            f.close()

            #open and read the file after the appending:
            f = open("output.txt", "r")
            print(f.read())


   


while True:
    inPut = Bank(input().upper())
    inPut.createAccount()
    inPut.createAccount()

    if inPut == "exit":
        print("thank you")
        break

    


