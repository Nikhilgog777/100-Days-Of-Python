import re

def count_vowels(text) :   #func to counting vowels
    return len(re.findall(r'[aeiou]', text, re.IGNORECASE))

name = "Nikhil Goswami"
print(name[3])  #Accessing a particular char using index
print(name[0:6])  #Slicing
print(count_vowels(name))  #called count_vowels funcn
print(name.upper())  #uppercase
print(name.lower())  #lowercase 
print(name[::-1]) #for reversing the name