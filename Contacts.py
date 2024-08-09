import json
import os
import re


FILENAME = 'contacts.json'


def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file)



def validate_email(email: str):
    email_regex = r"(^[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$)"
    _email = email
    while True:
        if _email == "cancel":
            return False
        if re.search(email_regex, _email) is not None:
            return _email
        else:
            _email = str(input("This Email is not valid!\nPlease try again or enter (cancel) to exit: \n"))

def validate_phone(phone_number: str):
    phone_regex = r"^(09|(\+989)|00989)[0-9]{9}$"
    _phone_number = phone_number
    while True:
        if _phone_number == "cancel":
            return False
        if re.search(phone_regex, _phone_number) is not None:
            return _phone_number
        else:
            _phone_number = str(input("This PhoneNumber is not valid!\nPlease try again or enter (cancel) to exit: \n"))

def validate_name(name:str):
    _name = name
    while True:
        if _name == "cancel":
            return False
        if _name not in contacts:
            return _name
        else:
            _name = str(input("This Name is already exist!\nPlease try again or enter (cancel) to exit: \n"))
    


def add_contact(contacts):
    name = validate_name(input("Enter Name:"))
    if name == False:
        return
    phone = validate_phone(input("Enter Phone:"))
    if phone == False:
        return
    email = validate_email(input("Enter Email:"))
    if email == False:
        return
    contacts[name] = {"phone":phone,"email":email}
    save_contacts(contacts)
    print(f"Added Contact {name}.")

def remove_contact(contacts):
    name = input("Enter the name of the contact you want to delete: \n")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} was deleted.")
    else:
        print("This Contact does not exist.")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: \n")
    if name in contacts:
        phone = validate_phone(input("Enter Phone:"))
        if phone == False:
            return
        email = validate_email(input("Enter Email:"))
        if email == False:
            return
        contacts[name] = {"phone":phone,"email":email}
        save_contacts(contacts)
        print(f"Contact {name} was edited.")
    else:
        print("This Contact does not exist.")

def display_contacts(contacts):
    if contacts:
        print("\nList of Contacts:")
        i = 1
        for name in contacts:
            print(f" {i} - Name: {name} - Phone Number: {contacts[name]['phone']} - Email: {contacts[name]['email']}")
            i += 1
    else:
        print("There are no Contacts.")

def display_sorted_contacts(contacts):
    if contacts:
        print("\nSorted list of Contacts (by Name):")
        _contacts = [x for x in contacts.keys()]
        _contacts.sort()

        i = 1
        for name in _contacts:
            print(f" {i} - Name: {name} - Phone Number: {contacts[name]['phone']} - Email: {contacts[name]['email']}")
            i += 1
    else:
        print("There are no Contacts.")



contacts = load_contacts()
while True:
    print("\n* Contacts Menue:")
    print("1 --> Add Contact")
    print("2 --> Edit Contact")
    print("3 --> Remove Contact")
    print("4 --> Show All Contact")
    print("5 --> Show All Contact (Sorted by Name)")
    print("6 --> Exit.")

    choice = input("* Enter the desired option: \n")

    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        edit_contact(contacts)
    elif choice == '3':
        remove_contact(contacts)
    elif choice == '4':
        display_contacts(contacts)
    elif choice == '5':
        display_sorted_contacts(contacts)
    elif choice == '6':
        break
    else:
        print("The option is invalid! Please try again...")

