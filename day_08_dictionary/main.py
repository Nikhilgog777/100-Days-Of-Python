# Build a “dictionary phonebook”: store 3 contacts (name: number) and let the user look up a name

phonebook = {
    "rohan" : 9034411111,
    "sohan" : 9034422222, 
    "mohan" : 9034433333
    }

search_name = input("Enter the name to search : ")

result = phonebook.get(search_name, f"Sorry {search_name} is not in the phonebook")

print(f"Name : {search_name} \nNumber : {result}")