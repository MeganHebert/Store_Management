#import uuid
#from datetime import datetime
#import Login 
import json

with open("athletic_tops.json","r") as tops:
    top_details = json.load(tops)
with open("athletic_bottoms.json","r") as bottoms:
    bottom_details = json.load(bottoms)
with open("athletic_acs.json","r") as acs:
    accessory_details = json.load(acs)


def browse_all_products():
    #with open("athletic_tops.json","r") as tops:
        #top_details = json.load(tops)
    print("TOPS")
    for tops in top_details:
        print(tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"]))
    print("\n")

    #with open("athletic_bottoms.json","r") as bottoms:
        #bottom_details = json.load(bottoms)
    print("BOTTOMS")
    for bottoms in bottom_details:
        print(bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"]))
    print("\n")

    #with open("athletic_acs.json","r") as acs:
        #accessory_details = json.load(acs)
    print("ACCESSORIES")
    for acs in accessory_details:
        print(acs["acs_desc"], "${}".format(acs["acs_price"])) 


def create_order():
    print("Would you like to look at:")
    print("[T]ops")
    print("[B]ottoms")
    print("[A]ccessories")

    while True:
        user_input = input()
        if user_input == "T" or "t":
           # with open("athletic_tops.json","r") as tops:
                #top_details = json.load(tops)
            for tops in top_details:
                print(tops["top_id"],tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"]))
            break
        elif user_input == "B" or "b":
            #with open("athletic_bottoms.json","r") as bottoms:
                #bottom_details = json.load(bottoms)
            print("BOTTOMS")
            for bottoms in bottom_details:
                print(bottoms["bottoms_id"],bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"]))
            break
        elif user_input == "A" or "a":
            #with open("athletic_acs.json","r") as acs:
                #accessory_details = json.load(acs)
            print("ACCESSORIES")
            for acs in accessory_details:
                print(acs["acs_id"],acs["acs_desc"], "${}".format(acs["acs_price"])) 
            break
        else: 
            print("Please enter t to browse tops, b to browse bottoms, or a to browse accessories")      

def home_page():
    print("Please choose from the following menu options:")
    print("[B]rowse Products")
    print("[C]reate Order")
    print("[P]ast Orders")

    while True:
        home_action = input()

        if home_action == "B" or "b":
            #browse_all_products()
            print("Please choose from the following menu options")
            print("[C]reate Order")
            print("[G]o back")
            print("[Q]uit")
            
            while True:
                user_input = input()
                if user_input == "C"or "c":
                    create_order()
                    break
                elif user_input == "G" or "g":
                    home_page()
                    break
                elif user_input == "Q" or 'q':
                    print("Thank you for visiting The Wild Bear!")
                    break
                else:
                    print("Please enter c to create an order, g to go back, or q to quit")
            break

        elif home_action == "C" or "c":
            create_order()
            break
        elif home_action == "P" or "p":
            break
        else:
            print("Please enter a b to browse products, c to create an order, or p to view your past orders")




    if home_action in ["B", "b"]:
        print("dads exa,")

# assign path module to __file__ (parameter) .parent -> wherever this executes, find what to look for in the parent of what were executing 
PATH = Path(__file__).parent / "newdata" to get subdirectory




 db.valid_users.find()


megan = user_actions.get_order_number()

                    if int(co_input) in range(0,count_top):
                        insert_lst = [{"orderID" : orderid, **top_details[int(co_input)-1]}]
                        db.orders.insert_many(insert_lst)
                        break
                    else:
                            print(f"Please input a valid product number within range: range{(1,count_top)}")
    #print(orders["Username"])

    #for item in orders:
        #print(item)
    orders_dict = {}
    while True:
        for item in orders:
            orders_dict.update(item)
            return orders_dict
    
print(orders_dict)

def admin_login(current_user: CurrentUser):
    current_user = CurrentUser()
    admin_dict = get_admin_dict()

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in admin_dict.keys() and admin_dict[username] == password:
            #current_user.store_user(username)
            print(f"Welcome Admin: {username}")
            #return current_user
            admin_actions.admin_home_page()
        else:
            print("Username or password is incorrect")