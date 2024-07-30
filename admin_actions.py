import json 
import logging
from pathlib import Path
from models import CurrentUser

PATH = Path(__file__).parent

def admin_home_page(admin_user: CurrentUser):
    while True:
        print("Please choose from the following menu:")
        print("[E]dit Inventory")
        print("[C]hange Product Price")
        print("[Q]uit")
        admin_hp_input = input()

        if admin_hp_input.upper() == "E":    
            print("Choose between the following product categories:")
            print("[T]ops")
            print("[B]ottoms")
            print("[A]ccessories")
            admin_prod_input = input()
            if admin_prod_input.upper() == "T":
                with open(PATH / "athletic_tops.json","r") as tops:
                    top_details = json.load(tops)
                print("Please choose from the following options: ")
                print("TOPS")

                for tops in top_details:
                    print([tops["top_id"]],tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"], tops["top_qt"]))
                    count_top = tops["top_id"]

                while True:
                    co_input = int(input("Enter the productID to modify: ").strip())
                    selected_top = next((top for top in top_details if top['top_id'] == co_input), None)
                    if selected_top:
                        new_quantity = int(input(f"Current quantity of {selected_top['top_desc']}, {selected_top['top_size']} is {selected_top['top_qt']}. Enter new quantity: ").strip())
                        selected_top['top_qt'] = new_quantity
                        logging.info(f'{admin_user.get_current_user()} has edited the quantity')
                        
                        with open(PATH / "athletic_tops.json", "w") as tops_file:
                            json.dump(top_details, tops_file, indent=4)

                        print("Would you like to:")
                        print("[C]ontinue")
                        print("[Q]uit")
                        while True: 
                            admin_cq_input = input()
                            if admin_cq_input.upper() == "C":
                                admin_home_page(admin_user)
                            elif admin_cq_input.upper() == "Q":
                                quit()
                            else:
                                print("Please enter c to continue or q to quit")

                    else:
                        print(f"Please input a valid product number within range: range{(1,count_top)}")

            elif admin_prod_input.upper() == "B":
                with open(PATH / "athletic_bottoms.json","r") as bottoms:
                    bottom_details = json.load(bottoms)
                    print("Please choose from the following options: ")
                    print("BOTTOMS")

                    for bottoms in bottom_details:
                        print([bottoms["bottom_id"]],bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"], bottoms["bottom_qt"]))
                        count_bottom = bottoms["bottom_id"]
                    co_input = int(input("Enter the productID to modify: ").strip())
                    selected_bottom= next((bottom for bottom in bottom_details if bottom['bottom_id'] == co_input), None)

                    if selected_bottom:
                        new_quantity = int(input(f"Current quantity of {selected_bottom["bottom_desc"]},{selected_bottom["bottom_size"]} is {selected_bottom['bottom_qt']}. Enter new quantity for {selected_bottom["bottom_desc"]} : ").strip())
                        selected_bottom['bottom_qt'] = new_quantity
                        logging.info(f'{admin_user.get_current_user()} has edited the quantity')
                        with open(PATH / "athletic_bottoms.json", "w") as bottoms_file:
                            json.dump(bottom_details, bottoms_file, indent=4)

                        print("Would you like to:")
                        print("[C]ontinue")
                        print("[Q]uit")
                        while True: 
                            admin_cq_input = input()
                            if admin_cq_input.upper() == "C":
                                admin_home_page(admin_user)
                            elif admin_cq_input.upper() == "Q":
                                quit()
                            else:
                                print("Please enter c to continue or q to quit")
                    else:
                        print(f"Please input a valid product number within range: range{(1,count_bottom)}")

            elif admin_prod_input.upper() == "A":
                with open(PATH / "athletic_acs.json","r") as acs:
                    accessory_details = json.load(acs)
                    print("Please choose from the following options: ")
                    print("ACCESSORIES")

                    for acs in accessory_details:
                        print([acs["acs_id"]], acs["acs_desc"], "${}".format(acs["acs_price"], acs["acs_qt"]))
                        count_acs = acs["acs_id"]
                    co_input = int(input("Enter the productID to modify: ").strip())
                    selected_acs= next((acs for acs in accessory_details if acs['acs_id'] == co_input), None)

                    if selected_acs:
                        new_quantity = int(input(f"Current quantity of {selected_acs["acs_desc"]} is {selected_acs['acs_qt']}. Enter new quantity for {selected_acs["acs_desc"]} : ").strip())
                        selected_acs['acs_qt'] = new_quantity
                        logging.info(f'{admin_user.get_current_user()} has edited the quantity')
                        with open(PATH / "athletic_acs.json", "w") as acs_file:
                            json.dump(accessory_details, acs_file, indent=4)

                        print("Would you like to:")
                        print("[C]ontinue")
                        print("[Q]uit")
                        while True: 
                            admin_cq_input = input()
                            if admin_cq_input.upper() == "C":
                                admin_home_page(admin_user)
                            elif admin_cq_input.upper() == "Q":
                                quit()
                            else:
                                print("Please enter c to continue or q to quit")
                    else:
                        print(f"Please input a valid product number within range: range{(1,count_acs)}")
                    
            else:
                print("Please enter a t for tops, b for bottoms, or a for accessories")
        elif admin_hp_input.upper() == "C":
            print("Choose between the following product categories:")
            print("[T]ops")
            print("[B]ottoms")
            print("[A]ccessories")
            admin_prod_input = input()
            while True:
                if admin_prod_input.upper() == "T":
                    with open(PATH / "athletic_tops.json","r") as tops:
                        top_details = json.load(tops)
                    print("Please choose from the following options: ")
                    print("TOPS")

                    for tops in top_details:
                        print([tops["top_id"]],tops["top_desc"], tops["top_size"], "${}".format(tops["top_price"], tops["top_qt"]))
                        count_top = tops["top_id"]

                    while True:
                        co_input = int(input("Enter the productID to modify: ").strip())
                        selected_top = next((top for top in top_details if top['top_id'] == co_input), None)
                        if selected_top:
                            new_price = int(input(f"Current price of {selected_top['top_desc']}, {selected_top['top_size']} is ${selected_top['top_price']}. Enter new price: ").strip())
                            selected_top['top_price'] = new_price
                            logging.info(f'{admin_user.get_current_user()} has edited the price')
                            with open(PATH / "athletic_tops.json", "w") as tops_file:
                                json.dump(top_details, tops_file, indent=4)

                            print("Would you like to:")
                            print("[C]ontinue")
                            print("[Q]uit")
                            while True: 
                                admin_cq_input = input()
                                if admin_cq_input.upper() == "C":
                                    admin_home_page(admin_user)
                                elif admin_cq_input.upper() == "Q":
                                    quit()
                                else:
                                    print("Please enter c to continue or q to quit")

                        else:
                            print(f"Please input a valid product number within range: range{(1,count_top)}")

                elif admin_prod_input.upper() == "B":
                    with open(PATH / "athletic_bottoms.json","r") as bottoms:
                        bottom_details = json.load(bottoms)
                    print("Please choose from the following options: ")
                    print("BOTTOMS")

                    for bottoms in bottom_details:
                        print([bottoms["bottom_id"]], bottoms["bottom_desc"], bottoms["bottom_size"], "${}".format(bottoms["bottom_price"], bottoms["bottom_qt"]))
                        count_top = bottoms["bottom_id"]

                    while True:
                        co_input = int(input("Enter the productID to modify: ").strip())
                        selected_bottom = next((bottom for bottom in bottom_details if bottom['bottom_id'] == co_input), None)
                        if selected_bottom:
                            new_price = int(input(f"Current price of {selected_bottom['bottom_desc']}, {selected_bottom['bottom_size']} is ${selected_bottom['bottom_price']}. Enter new price: ").strip())
                            selected_bottom['bottom_price'] = new_price
                            logging.info(f'{admin_user.get_current_user()} has edited the price')
                            with open(PATH / "athletic_bottoms.json", "w") as bottoms_file:
                                json.dump(bottom_details, bottoms_file, indent=4)

                                print("Would you like to:")
                                print("[C]ontinue")
                                print("[Q]uit")
                                while True: 
                                    admin_cq_input = input()
                                    if admin_cq_input.upper() == "C":
                                        admin_home_page(admin_user)
                                    elif admin_cq_input.upper() == "Q":
                                        quit()
                                    else:
                                        print("Please enter c to continue or q to quit")
                        else:
                            print(f"Please input a valid product number within range: range{(1,count_top)}")
                elif admin_prod_input.upper() == "A":
                    with open(PATH / "athletic_acs.json","r") as acs:
                        accessory_details = json.load(acs)
                    print("Please choose from the following options: ")
                    print("ACCESSORIES")

                    for acs in accessory_details:
                        print([acs["acs_id"]], acs["acs_desc"], "${}".format(acs["acs_price"], acs["acs_qt"]))
                        count_acs = acs["acs_id"]
                    co_input = int(input("Enter the productID to modify: ").strip())
                    selected_acs= next((acs for acs in accessory_details if acs['acs_id'] == co_input), None)

                    if selected_acs:
                        new_quantity = int(input(f"Current price of {selected_acs["acs_desc"]} is ${selected_acs['acs_price']}. Enter new price for {selected_acs["acs_desc"]} : ").strip())
                        selected_acs['acs_qt'] = new_quantity
                        logging.info(f'{admin_user.get_current_user()} has edited the price')
                        with open(PATH / "athletic_acs.json", "w") as acs_file:
                            json.dump(accessory_details, acs_file, indent=4)

                            print("Would you like to:")
                            print("[C]ontinue")
                            print("[Q]uit")
                            while True: 
                                admin_cq_input = input()
                                if admin_cq_input.upper() == "C":
                                    admin_home_page(admin_user)
                                elif admin_cq_input.upper() == "Q":
                                    quit()
                                else:
                                    print("Please enter c to continue or q to quit")
                    else:
                        print(f"Please input a valid product number within range: range{(1,count_acs)}")
                
                else:
                    print("Please enter a t for tops, b for bottoms, or a for accessories")                        
        elif admin_hp_input.upper() == "Q":
            quit()
        else:
            print("Please enter e to edit inventory, c to change a product price, or q to quit")
