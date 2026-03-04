# Get the Enviroment from user and print it out

env = input("Please enter your environment: ") # input() function is used to take input from the user
print("Your environment is:", env)

# type casting
# type casting is the process of converting one data type to another data type. In Python, you can use the built-in functions to perform type casting. For example, you can use int() to convert a string to an integer, float() to convert a string to a float, and str() to convert a number to a string.
# Example of type casting
num_str = "100" # num_str is a string
num_int = int(num_str) # num_int is an integer
print(num_int) # Output: 100
print(type(num_int)) # Output: <class 'int'>  

# Conditional Statements
# simple if else statement
if env == "production":
    print("Don't Deploy on friday")
elif env == "staging":
    print("You are in staging environment \n take care of your data and don't deploy on friday  ")
else:
    print("You can deploy on any days")


x = int(input("Please Enter a  num _1 : "))
y = int(input("Please Enter a  num _2 : "))
sum = x + y
print("The sum of num_1 and num_2 is:", sum)    
print(type(sum)) # Output: <class 'int'>

print("Subtraction of num_1 and num_2 is:", x - y)
print("Multiplication of num_1 and num_2 is:", x * y)
print("Division of num_1 and num_2 is:", x / y)
print("Floor Division of num_1 and num_2 is:", x // y)
print("Exponentiation of num_1 and num_2 is:", x ** y)
print("Modulus of num_1 and num_2 is:", x % y)
