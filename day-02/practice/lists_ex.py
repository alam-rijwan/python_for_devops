# 1st method to create a list
a = [100, 200, 300,True, False, "Hello", "World", 3.14] # List of different data types  
a.append("DevOps") # Adding an element to the end of the list
print(a)


# 2nd method to create a list
clouds = list(["AWS", "Azure", "GCP"]) # Creating a list using the list() constructor
clouds.append('Oracle Cloud') # Adding an element to the end of the list
clouds.insert(1, 'IBM Cloud') # Inserting an element at a specific index (index 1 in this case) 
clouds[0] = 'Amazon Web Services' # Modifying an element at a specific index (index 0 in this case) 
clouds.remove('GCP') # Removing an element from the list by value
clouds.append("Alibaba Cloud") # Adding another element to the end of the list
clouds.append('GCP') # Adding 'GCP' back to the end of the list


print(clouds)
print('Length of the clouds list:', len(clouds)) # Printing the length of the list

print('Index of Azure:', clouds.index('Azure')) # Finding the index of an element in the list
print('Worlds leader of:', clouds[0]) # Accessing the first element of the list

# 3rd method to create a list
numbers = list(range(1, 11)) # Creating a list of numbers from 1 to 10 using the range() function
print(numbers)  

