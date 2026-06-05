# Create a simple “contact manager” that saves contacts to a JSON file (load, add, save).

import json 
import os

FILENAME = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file. Creates an empty file if none exists."""
    if not os.path.exists(FILENAME):
        return[]
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONecodeError:
        print("Warning: JSON file was corrupted. Starting with empty list.")
        return []

def save_contacts(contacts):
    """Saves the current contacts list back to the JSON file."""
    try: 
        with open(FILENAME, "w") as file:
            json.dump(contacts, file, indent = 4)
        print("System: Contacts saved successfully.")
    except IOError:
        print("Error: Could not write to file.")

def add_contact(contacts):
    """Prompts user for details and appends a new contact to the list."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    if not name : 
        print("Error: Name field cannot be empty.")
        return 
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    print(f"System: Added '{name}' to temporary lsit.")
    
    # Auto-save immediately after adding
    save_contacts(contacts)

def list_contacts(contacts):
    """Displays all saved contacts."""
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return 
    
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

def main():
    """Main program execution loop."""
    contacts = load_contacts()

    while True : 
        print("\n=== Contact Manager ====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2" : 
            add_contact(contacts)
        elif choice == "3" : 
            print("Goodbye!")
            break
        else: 
            print("Invalid selection. Please try again.")

if __name__ == "__main__" : 
    main()