import random

database = {}  # Corrected this variable call


def init():
    
    print("Welcome to Bank Express")
    
    haveAccount = int(input("Do you have a account with us: 1 (yes) 2 (no) \n"))
    
    if (haveAccount == 1):
        
            login()
    elif (haveAccount == 2):
            
          register()
            
    else:
        print("You have selected invalid option")
        init()


def login():
    
    print("*****Login*****")

    accountNumberFromUser = int(input("Please type your account number. \n"))
    password = input("Please type your password. \n")
    
    for accountNumber ,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3]) == password):
            bankOperation(userDetails)


    print("Invalid account or password")
    



def register():
    print("*****Registration*****")

    email = input("What is your email address?")
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    password = input("Create a password \n")  

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password ]

    print("Welcome, your account has been created.")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure to not share your password to prevent account theft.")
    print(" == ==== ====== ===== ==")

    login()

def bankOperation(user):
    print("Welcome %s %s" % ( user[0], user[1] ) )
    
    selectedOption = int(input("Pick a option to do. (1) deposit (2) withdrawal (3) Logout (4) Exit"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

            withdrawalOperation()
    elif(selectedOption == 3):

            login()
    elif(selectedOption == 4)
    exit()
    
    else:
    print("Invaild option selected")
    bankOperation(user)

def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit Operation")


def generationAccountNumber():
    
    print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)

def logout
# print(generationAccountNumber())

init()
