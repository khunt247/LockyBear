"""
    Takes in an entity name and password and saves it in a file.

    Args:
        entity_name (str): The name of the entity (used for filename)
        password (str): The password to save

    The password is saved in a file named "<entity_name>.passwd"
    """


import io
import os

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    f = io.open(file, "w")
    print(f"File '{f}' password created!")
    f.write(password)
    print(f" '{password}' Password saved successfully")
    f.close()

def retrieve_password(entity_name):
    file = entity_name + ".passwd"
    if os.path.exists("file"):
        f = io.open(file, "r")
        content = f.read()
        print(f"Password is {content}.")
        f.close()
        return data
    else:
        return "Error"
