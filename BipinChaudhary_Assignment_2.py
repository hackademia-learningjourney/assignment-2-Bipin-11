'''
Question : WAP that first gives 2 options:
            1. Sign up
            2. Sign in

            when 1 is pressed user needs to provide following information
            Username, 2. Password, 3. Mobile number All this information is saved in a file everytime a new user signs up the same file is updated
            (hint Append over the same file)

            when 2 is pressed User needs to provide username and password this username and password is checked with username and password in the 
            database
            if matched: 
                welcome to the device and show their phone number 
            else: 
                terminate the program saying incorrect credentials

Do it using json files, save everything to json and load from json
'''

import json
import os

userdata_file = 'assignment-2-Bipin-11/user_data.json'

def load_user_data():
    if os.path.exists(userdata_file):
        with open(userdata_file, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    with open(userdata_file, 'w') as file:
        json.dump(user_data, file, indent=4)

def sign_up():
    user_data = load_user_data()

    username = input("Enter username: ")
    if username in user_data:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Enter password: ")
    mobile_number = input("Enter mobile number: ")

    user_data[username] = {
        'password': password,
        'mobile_number': mobile_number
    }

    save_user_data(user_data)
    print("Sign up successful!")

def sign_in():
    user_data = load_user_data()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device! Your mobile number is: {user_data[username]['mobile_number']}")
    else:
        print("Incorrect credentials. Terminating the program.")


print("1. Sign up")
print("2. Sign in")

choice = input("Select an option (1 or 2): ")

if choice == '1':
    sign_up()
elif choice == '2':
    sign_in()
else:
    print("Invalid choice. Exiting.")
