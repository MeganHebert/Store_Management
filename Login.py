from pymongo import MongoClient
from models import User
from models import UserList
from models import CurrentUser

client = MongoClient()
db = client.get_database("wildbeardb")

# gets user accounta data from db
def get_db_accounts():
    accounts = db.accounts.find()
    return accounts

# converts db accounts data into userList object w/ user instances 
def get_user_list():
    accounts = get_db_accounts()
    ul = UserList()

    for acc in accounts:
        user = User(
            username=acc["username"],
            password=acc.get("password"),              #.get will allow for no key value: password
        )
        ul.user_list.append(user)
    
    return ul

# converts userList object into dictionary
def get_user_dict():
    ul = get_user_list()
    user_dict = {}
    
    for user in ul.user_list:
        user_dict.update(user.user_dict())
    
    return user_dict

# load admin from json -> put in db
def get_admin_db():
    admin_acc = db.admin.find()
    return admin_acc

def get_admin_list():
    accounts = get_admin_db()
    admin_ul = UserList()

    for acc in accounts:
        admin_user = User(
            username=acc["username"],
            password=acc.get("password"),              #.get will allow for no key value: password
        )
        admin_ul.user_list.append(admin_user)
    
    return admin_ul

def get_admin_dict():
    ul = get_admin_list()
    admin_dict = {}
    
    for user in ul.user_list:
        admin_dict.update(user.user_dict())

    return admin_dict


def initial_login():
    print("Welcome to The Wild Bear, a workout clothing line \n")
    print("To begin please [L]ogin or [C]reate Account:")

    while True: 
        init_login = input()                # L or C
        init_login = init_login.strip()

        if init_login == 'l' or init_login == 'L':
            print("Thank you for returning to The Wild Bear! \nPlease specify whether you're and [A]dmin or regular [U]ser:")

            while True: 
                l_login = input()               # A or U
                l_login = l_login.strip()

                if l_login == 'a' or l_login =="A":
                    current_user: CurrentUser = admin_login()
                    return current_user
                elif l_login == 'u' or l_login == 'U':
                    current_user: CurrentUser = user_login()
                    return current_user
                else:
                    print("Please enter A for Admin or U for user.")
        elif init_login == 'c' or init_login == "C":
            register()
            break
        else: 
            print("Please enter L for Login or C to Create Account.")


def register():
    user_dict = get_user_dict()

    while True: 
        username = input("Create username: ")

        if len(username) > 4: 
            if username not in user_dict.keys():
                break
            else:
                print("This username already exists. Please enter a new one")

        else:
                print("Please enter a username with more than 4 characters") 

    while True:
        password = input("Create password: ")

        if len(password) > 5:
            break
        else:
            print("Please enter a password with more 5 than characters")
    
    db.accounts.insert_one({"username": username, "password": password})

def user_login():
    current_user = CurrentUser()

    user_dict = get_user_dict()

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in user_dict.keys() and user_dict[username] == password:
            current_user.store_user(username)
            print(f'\nWelcome {username}')
            return current_user
        else:
            print("Username or password is incorrect")
        
def admin_login():
    admin_dict = get_admin_dict()

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in admin_dict.keys() and admin_dict[username] == password:
            current_user = CurrentUser(is_admin=True)
            current_user.store_user(username)
            print(f"Welcome Admin: {username}")
            return current_user
        else:
            print("Username or password is incorrect")

        


