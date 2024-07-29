import json
import random
from pathlib import Path
from pymongo import MongoClient

client = MongoClient()
db = client.get_database("wildbeardb")

PATH = Path(__file__).parent

def get_order_number():
    order_id = random.sample()
    print(order_id)
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


def create_order():
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

                if int(co_input) in range(0,count_top):
                    print(top_details[int(co_input)-1])

                    break
                else:
                    print(f"Please input a valid product number within range: range{(1,count_top)}")
            break
        elif user_input.upper() == "B":
            with open(PATH / "athletic_bottoms.json","r") as bottoms:
                bottom_details = json.load(bottoms)
            print("Please choose from the following options: ")
            print("BOTTOMS")
            for bottoms in bottom_details:
                print([bottoms["bottom_id"]],bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"]))
            break
        elif user_input.upper() == "A":
            with open(PATH / "athletic_acs.json","r") as acs:
                accessory_details = json.load(acs)
            print("Please choose from the following options: ")
            print("ACCESSORIES")
            for acs in accessory_details:
                print([acs["acs_id"]],acs["acs_desc"], "${}".format(acs["acs_price"])) 
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
        if home_action.upper() == "B":   
            browse_all_products()
            print("Please choose from the following menu options")
            print("[C]reate Order")
            print("[G]o back")
            print("[Q]uit")
                        
            while True:
                user_input = input()
                if user_input.upper() == "C":
                    create_order()
                    break
                elif user_input.upper() == "G":
                    home_page()
                    break
                elif user_input.upper() == "Q":
                    print("Thank you for visiting The Wild Bear!")
                    break
                else:
                    print("Please enter c to create an order, g to go back, or q to quit")
            break
        elif home_action.upper() == "C":
            create_order()
            break
        elif home_action.upper() == "P":
            print("past works")
            break
        else:
            print("Please enter a b to browse products, c to create an order, or p to view your past orders")
