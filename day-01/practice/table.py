 # Table program
# Take input from the user
num = int(input("Please enter a number of you want table for : "))
 # input() function is used to take input from the user and int() function is used to convert the input to an integer

# strinng formatting
for i in range(1 , 11):
 print(f"{num} x {i} = {num*i}") # f-string is used for string formatting and {num} is used to insert the value of num in the string and {i} is used to insert the value of i in the string and {num*i} is used to insert the value of num*i in the string  
 