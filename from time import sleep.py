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

# user name, password, 
class Bank:
    def __init__(self,initput):
        self.input = initput
    def loggin(self):
        self.log = input("please type in your bank card number: ")
        self.i = 0
        self.p = 9999999999
        Bank.info = []
        
        with open('output.txt','r') as file:
            for line in file:
                for word in line.split():
                    self.i = self.i + 1
                    if self.log == word:
                        self.p = self.i
                    if self.i >= self.p and self.i<=self.p+5:
                        Bank.info.append(word)
                self.i = 0
        print(Bank.info)
        self.passW = getpass(prompt="Password: 🔒 ")
        pas= Bank.info[1]
        while self.passW != pas:
            print("Password wrong!!!")
            self.passW = getpass(prompt="Password again: 🔒 ")
            if self.passW == "exit":
                break
        # Bank(1).Deposit(self.info)

    



    def createAccount(self):
        if self.input == "Create account".upper():
            self.balance = 0.00
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
            print("Welcome to our bank! Your bank card number is: ", self.number)
            f = open("output.txt", "a")
            self.array = [str(self.number)," ",self.password," ",self.name," ",self.email," ",self.phone," ",str(self.balance)]
            for self.bb in self.array:
                f.write(self.bb)
            f.write("\n")
            f.close()

    def Withdraw(self):
        print(len(Bank.info))
        self.mybalance = float(Bank.info[5])
        self.withdraw = True
        self.withdraw = float(input("Please enter the withdraw amount: "))
        if (self.mybalance < self.withdraw):
            print("Sorry you don't have enough balance. ")
        else:
            self.mybalance = self.mybalance - self.withdraw
        search = Bank.info[0]+" "+Bank.info[1]+ " "+ Bank.info[2]+" "+Bank.info[3]+" "+ Bank.info[4]+" "+ Bank.info[5]
        replace = Bank.info[0]+" "+Bank.info[1]+ " "+ Bank.info[2]+" "+Bank.info[3]+" "+ Bank.info[4]+" "+ str(self.mybalance)
        fin = open("output.txt", "rt")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace(search, replace)
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open("output.txt", "wt")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()
        self.ii = 0
        self.pp = 0
        with open('output.txt','r') as file:
            for line in file:
                for word in line.split():
                    self.ii = self.ii + 1
                    if Bank.info[0] == word:
                        self.pp = self.ii
                        Bank.info = []
                    if self.ii >= self.pp and self.ii<=self.pp+5:
                        Bank.info.append(word)
                self.ii = 0
        print(Bank.info)

    def Deposit(self):
        self.myBalance = float(Bank.info[5])
        self.deposit = True
        self.deposit = float(input("Please enter the deposit amount: "))
        while self.deposit < 0:
            self.deposit("Please enter the positive amount: ")
        self.myBalance = self.myBalance + self.deposit
        Search = Bank.info[0]+" "+Bank.info[1]+ " "+ Bank.info[2]+" "+Bank.info[3]+" "+ Bank.info[4]+" "+ Bank.info[5]
        Replace = Bank.info[0]+" "+Bank.info[1]+ " "+ Bank.info[2]+" "+Bank.info[3]+" "+ Bank.info[4]+" "+ str(self.myBalance)
        Fin = open("output.txt", "rt")
        #read file contents to string
        Data = Fin.read()
        #replace all occurrences of the required string
        Data = Data.replace(Search, Replace)
        #close the input file
        Fin.close()
        #open the input file in write mode
        Fin = open("output.txt", "wt")
        #overrite the input file with the resulting data
        Fin.write(Data)
        #close the file
        Fin.close()
        self.iii = 0
        self.ppp = 0
        with open('output.txt','r') as file:
            for line in file:
                for word in line.split():
                    self.iii = self.iii + 1
                    if Bank.info[0] == word:
                        self.ppp = self.iii
                        Bank.info = []
                    if self.iii >= self.ppp and self.iii<=self.ppp+5:
                        Bank.info.append(word)
                self.iii = 0
        print(Bank.info)
        


   


while True:
    inPut = input().upper()
    if  inPut == "Create account".upper():
        Bank(inPut).createAccount()
    if  inPut == "Deposit".upper():
        Bank(inPut).Deposit()
    if  inPut == "Withdraw".upper():
        Bank(inPut).Withdraw()
    if inPut == "SHOW EVERYTHING":
        with open('output.txt','r') as file:
            for line in file:
                for word in line.split():
                    print(word) 
    if inPut == "Loggin".upper():
        Bank(inPut).loggin()
    

    if inPut == "LOGOUT":
        print("thank you")
        break

# #read input file
# fin = open("output.txt", "rt")
# #read file contents to string
# data = fin.read()
# #replace all occurrences of the required string
# apple = "a "+"b "+ "c"
# data = data.replace(apple, 'python')
# #close the input file
# fin.close()
# #open the input file in write mode
# fin = open("output.txt", "wt")
# #overrite the input file with the resulting data
# fin.write(data)
# #close the file
# fin.close()

    


