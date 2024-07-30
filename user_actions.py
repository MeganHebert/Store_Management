import json
import random
import datetime
import logging
from Login import CurrentUser 
from pathlib import Path
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
db = client.get_database("wildbeardb")

PATH = Path(__file__).parent

def get_db_orders():
    cust_orders = db.orders.find()
    logging.info("Open orders db")
    return cust_orders

def get_order_number():
    num_users = range(1,50000)
    order_id = random.sample(num_users,1)[0]
    return order_id

def browse_all_products():
    with open(PATH / "athletic_tops.json","r") as tops:
        top_details = json.load(tops)
    print("TOPS")
    for tops in top_details:
        print(tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"]))
    print("\n")

    with open(PATH / "athletic_bottoms.json","r") as bottoms:
        bottom_details = json.load(bottoms)
    print("BOTTOMS")
    for bottoms in bottom_details:
        print(bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"]))
    print("\n")

    with open(PATH / "athletic_acs.json","r") as acs:
        accessory_details = json.load(acs)
    print("ACCESSORIES")
    for acs in accessory_details:
        print(acs["acs_desc"], "${}".format(acs["acs_price"])) 

def create_order_menu(current_user: CurrentUser):
    print("Would you like to:")
    print("[H]ome Menu")
    print("[C]ontinue shopping")
    print("[Q]uit")

    while True:
        user_input = input()
        if user_input.upper() == "H":
            home_page(current_user)
        elif user_input.upper() == "C":
            create_order(current_user)
        elif user_input.upper() == "Q":
            print("Thank you for visiting The Wild Bear")
            quit()
        else: 
            print("Please enter h for home menu, c to continue shopping, or q to quit")

orderid = get_order_number()

def create_order(current_user: CurrentUser):
    time_stamp = datetime.datetime.now()
    get_db_orders()
    print("Would you like to look at:")
    print("[T]ops")
    print("[B]ottoms")
    print("[A]ccessories")

    while True:
        user_input = input()
        print("\n")
        if user_input.upper() == "T":
            with open(PATH / "athletic_tops.json","r") as tops:
                top_details = json.load(tops)
            print("Please choose from the following options: ")
            print("TOPS")
            get_order_number()
            for tops in top_details:
                print([tops["top_id"]],tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"]))
            count_top = tops["top_id"] 

            while True:
                co_input = input()
                username = current_user.get_current_user()
                index = int(co_input)
 
                if int(co_input) in range(0,count_top + 1):
                    selected_top = top_details[index-1]
                    selected_top["top_qt"] -=1
                    with open(PATH / "athletic_tops.json", "w") as tops_file:
                        json.dump(top_details, tops_file, indent=4)
                    print(f"Order placed for {selected_top['top_desc']}, {selected_top['top_size']}!")

                    insert_lst = [{"orderID" : orderid, "Username": username, **top_details[int(co_input)-1], "Date": time_stamp}]
                    db.orders.insert_many(insert_lst)
                    db.orders.update_many({}, {'$unset' : {"top_qt": ""}}) 
                    logging.info("Top order created")

                    create_order_menu(current_user)
                    break
                else:
                    print(f"Please input a valid product number within range: range{(1,count_top)}")

        elif user_input.upper() == "B":
            with open(PATH / "athletic_bottoms.json","r") as bottoms:
                bottom_details = json.load(bottoms)
            print("Please choose from the following options: ")
            print("BOTTOMS")
            for bottoms in bottom_details:
                print([bottoms["bottom_id"]],bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"]))
            count_bottom = bottoms["bottom_id"]

            while True:
                co_input = input()
                username = current_user.get_current_user()
                index = int(co_input)

                if int(co_input) in range(0,count_bottom +1):
                    selected_bottom = bottom_details[index -1]
                    selected_bottom["bottom_qt"] -=1
                    with open(PATH / "athletic_bottoms.json", "w") as bottoms_file:
                        json.dump(bottom_details, bottoms_file, indent=4)
                    print(f"Order placed for {selected_bottom['bottom_desc']}, {selected_bottom['bottom_size']}!")

                    insert_lst = [{"orderID" : orderid, "Username": username, **bottom_details[int(co_input)-1], "Date": time_stamp}]
                    db.orders.insert_many(insert_lst)
                    db.orders.update_many({}, {'$unset' : {"bottom_qt": ""}}) 
                    logging.info("Bottom order created")
                    create_order_menu(current_user)
                    break
                else:
                    print(f"Please input a valid product number within range: range{(1,count_bottom)}")
            break

        elif user_input.upper() == "A":
            with open(PATH / "athletic_acs.json","r") as acs:
                accessory_details = json.load(acs)
            print("Please choose from the following options: ")
            print("ACCESSORIES")
            for acs in accessory_details:
                print([acs["acs_id"]],acs["acs_desc"], "${}".format(acs["acs_price"])) 
            count_acs = acs["acs_id"]

            while True:
                co_input = input()
                username = current_user.get_current_user()
                index = int(co_input)

                if int(co_input) in range(0,count_acs +1):
                    selected_acs = accessory_details[index -1]
                    selected_acs["acs_qt"] -=1
                    with open(PATH / "athletic_acs.json", "w") as acs_file:
                        json.dump(accessory_details, acs_file, indent=4)
                    print(f"Order placed for {selected_acs['acs_desc']}!")

                    insert_lst = [{"orderID" : orderid, "Username": username, **accessory_details[int(co_input)-1], "Date": time_stamp}]
                    db.orders.insert_many(insert_lst)
                    db.orders.update_many({}, {'$unset' : {"acs_qt": ""}}) 
                    logging.info("Accessory order created")
                    create_order_menu(current_user)
                    break
                else:
                    print(f"Please input a valid product number within range: range{(1,count_acs)}")
            break
        else: 
            print("Please enter t to browse tops, b to browse bottoms, or a to browse accessories")    

def get_past_orders(current_user: CurrentUser):
    past_orders = db.orders
    search_key = current_user.get_current_user()
    #orders = past_orders.find({"Username": search_key})
    cursor = past_orders.find({})

    with open('past_orders.json', 'w') as file:
        json.dump(json.loads(dumps(cursor)),file)

    with open('past_orders.json', 'r') as past_order:
        all_past_orders = json.load(past_order)

    for order in all_past_orders:
        if order['Username'] == search_key:
            order.pop('_id')
            print(order)
        else:
            pass
    
    home_page(current_user)

def home_page(current_user: CurrentUser):
    print("Please choose from the following menu options:")
    print("[B]rowse Products")
    print("[C]reate Order")
    print("[P]ast Orders")
    print("[Q]uit")

    while True:
        home_action = input()
        if home_action.upper() == "B":   
            browse_all_products()
            print("Please choose from the following menu options")
            print("[C]reate Order")
            print("[G]o back")
            print("[Q]uit")
                        
            while True:
                user_input = input()
                if user_input.upper() == "C":
                    create_order(current_user)
                    break
                elif user_input.upper() == "G":
                    home_page(current_user)
                    break
                elif user_input.upper() == "Q":
                    print("Thank you for visiting The Wild Bear!")
                    break
                else:
                    print("Please enter c to create an order, g to go back, or q to quit")
            break
        elif home_action.upper() == "C":
            create_order(current_user)
        elif home_action.upper() == "P":
            get_past_orders(current_user)
        elif home_action.upper() == "Q":
            quit()
        else:
            print("Please enter a b to browse products, c to create an order, p to view your past orders, or q to quit")
