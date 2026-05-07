# Dictionary is a collection of key-value pairs. It is unordered, mutable and indexed. It is defined by using curly braces {}.
info = {
    "name" : "Rijwan Alam", # String
    "qualification" : "B.Sc IT",# String
    "city" : "Mumbai",# String
    "age" :26,# Integer
    "salary" : 23.5,# Float
    "married" : False ,#Boolean
    "skills" : ["Python", "Docker", "Linux", "AWS"] #list


}
print('I live in', info["city"]) # Accessing the value of a key in the dictionary
print('My skills are', info.get("skill", "not found")) 

info.update({"experience" : 2}) # Adding a new key-value pair to the dictionary
print(info)

print(dir(info)) # Printing the methods of the dictionary

#for i in info:
 #   print(i)
# iterat a dict 
for key,value in info.items():
    print(key,value)