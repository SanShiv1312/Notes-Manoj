# Created by Manoj Paramsetti

import pymongo

import getpass

myclient = pymongo.MongoClient("mongodb://localhost:27017")
my_db = myclient["Instagram-Clone"]
my_collection = my_db["users"]

RUNNER = True

while RUNNER:
    Input = input("1. Sign In\n2. Login\n3. Update username or password\n4. Delete account\n5. exit\n>> ").lower()

    if Input == "1":
        username = input("Enter your username: ")
        password = getpass.getpass(prompt="Enter your password: ")
        inserting_data={"user": username, "password": password}
        data_from_db = my_collection.find_one({"user" : username})
        
        if data_from_db == None:
            my_collection.insert_one(inserting_data)
        else:
            print("Account already exits, try to login")

    elif Input == "2":
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        query = {"user": username, "password": password}
        data_from_db = my_collection.find_one(query)
        
        if data_from_db != None:
            print("Logged In, Successfully")
            RUNNER = False
        
        else:
            print("Wrong username or password")
    elif Input == "3":
        update = input("update\n======\n1. Username\n2. Password\n>> ")
        username = input("\nEnter Username: ")
        password = getpass.getpass("Enter Password: ") 
        query = { "user": username, "password": password }
        data_from_db = my_collection.find_one(query)

        if data_from_db != None:
            if update == "1":
                old_data = query
                new_username = input("Enter new username: ")
                new_data = {"$set": {"user": new_username}}
                my_collection.update_one(old_data, new_data)
                print("Updated\n")
            elif update == "2":
                old_data = query
                new_password = input("Enter new password: ")
                new_data = {"$set": {"password": new_password}}
                my_collection.update_one(old_data, new_data)
                print("Updated\n")
            else:
                print("Wrong Input")
    elif Input == "4":
        username = input("\nEnter Username: ")
        password = getpass.getpass("Enter Password: ") 
        query = { "user": username, "password": password }
        data_from_db = my_collection.find_one(query)

        if data_from_db != None:
            my_collection.delete_one(query)
        else:
            print("Wrong password or username")
    elif Input == "5":
        RUNNER = False
    
    else:
        print("Incorrect Input")
