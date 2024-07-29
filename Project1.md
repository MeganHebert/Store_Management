
# load json file into a object, using json function called load.. open file first
with open('orders.json') as f:
    orders_data = json.load(f)





# creates unique userID
def get_next_user_id():
    counter_doc = db.counters.find_one_and_update(
        {"_id": "user_id"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    return counter_doc['seq']


def register():
    user_id = get_next_user_id()
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
            #continue
    
    db.accounts.insert_one({"_id": user_id, "username": username, "password": password})
    user_login()

j = current_user.get_current_user()
    print(j)





# Function to get a specific top_desc
def get_specific_top_desc(data, target_desc):
    for item in data:
        if item['top_desc'] == target_desc:
            return item

    return None  # If not found

# Example usage:
target_description = "Black T-Shirt"
specific_top = get_specific_top_desc(json_data, target_description)

if specific_top:
    print("Found top details:")
    print(f"Top ID: {specific_top['top_id']}")
    print(f"Top Size: {specific_top['top_size']}")
    print(f"Top Price: ${specific_top['top_price']}")
    print(f"Top Quantity: {specific_top['top_qt']}")
else:
    print(f"Top with description '{target_description}' not found.")




# Convert JSON to DataFrame
df = pd.json_normalize(data)

# Print DataFrame with aligned columns
print(df.to_string(index=False))