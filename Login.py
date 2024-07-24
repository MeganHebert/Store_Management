from pymongo import MongoClient

client = MongoClient()

db = client.get_database("wildbeardb")


def initial_login():
    print("Welcome to The Wild Bear, a workout clothing line \n")
    print("To begin please [L]ogin or [C]reate Account:")

    while True: 
        init_login = input()                # L or C
        init_login = init_login.strip()

        if init_login == 'l' or init_login == 'L':
            print("Thank you for returning to The Wild Bear! \n Please specify whether you're and [A]dmin or regular [U]ser:")

            while True: 
                l_login = input()               # A or U
                l_login = l_login.strip()

                if l_login == 'a' or l_login =="A":
                    print("admin works")
                    break
                elif l_login == 'u' or l_login == 'U':
                    print("user works")
                    break
                else:
                    print("Please enter A for Admin or U for user.")

            break
        elif init_login == 'c' or init_login == "C":
            register()
            break
        else: 
            print("Please enter L for Login or C to Create Account.")
        

def register():
    #username = input("Create username: ")
    #password = input("Create password: ")
    #init_client()
    while True: 
        username = input("Create username: ")

        if len(username) > 4:
            break
        else:
            print("Please enter a username with more than 4 characters")
    
    while True:
        password = input("Create password: ")

        if len(password) > 5:
            break
        else:
            print("Please enter a password with more 5 than characters")


    
    db.accounts.insertone({"username": username}, {"password": password})





