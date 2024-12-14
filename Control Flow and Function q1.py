#Task
#1. Large Power
#Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:
#Define the function to accept two input parameters called base and exponent
#Calculate the result of base to the power of exponent
#Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False

#Coding Question
#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False

# Define the function large_power
def large_power(base, exponent):
    # Calculate the result of base raised to the power of exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Ask the user for input
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Call the function and print the result
if large_power(base, exponent):
    print("The result is greater than 5000: True")
else:
    print("The result is not greater than 5000: False")
