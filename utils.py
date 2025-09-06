"""
    Takes in an entity name and password and saves it in a file.

    Args:
        entity_name (str): The name of the entity (used for filename)
        password (str): The password to save

    The password is saved in a file named "<entity_name>.passwd"
    """

import os

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    f = open(file, "w")
    f.write(password)
    print("Password saved successfully")
    print(file)
    f.close()

def retrieve_password(entity_name):
    file = entity_name + ".passwd"
    if os.path.exists(file):
        f = open(file, "r")
        data = f.read()
        print("Password retrieved successfully")
        print(data)
        f.close()
        return data
    else:
        return "error"
