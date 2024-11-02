# Python-Functions
#
# 1.	What does the len() function do in Python?
# Write a code example using len() to find the length of a list.

# The len() function in Python returns the number of items in an object.
# This can be used with various data types,
# such as strings, lists, tuples, and dictionaries.
#list=[32,25,10,5,28]
#print (len(list))

# 2.	Write a Python function greet(name) that takes a person's
# name as input and prints "Hello, [name]!".

# def greet(name):
#    print("Hello,[name]!")
# greet("Hello,[name]!")

# 3.	.Write a Python function find_maximum(numbers) that takes a
# # list of integers and returns the maximum value without using the built-in max() function.
# # Use a loop to iterate through the list and compare values

# def find_maximum(numbers):
#     # Assume the first number is the maximum
#     if not numbers:
#         return None  # Handle empty list case
#
#     maximum = numbers[0]
#
#     # Iterate through the list and compare values
#     for number in numbers:
#         if number > maximum:
#             maximum = number
#
#     return maximum
#
#
# # Example usage
# numbers_list = [31, 15, 21, 68, 12]
# maximum_value = find_maximum(numbers_list)
# print(f"The maximum value in the list is: {maximum_value}")

#Explanation related to the loop
# The function first checks if the list is empty and returns None if it is.
# It initializes maximum to the first element of the list.
# It then iterates through each number in the list, updating maximum whenever it finds a larger value.
# Finally, it returns the maximum value found.


# 4.	Explain the difference between local and global variables in a Python function.
# Write a program where a global variable and a local variable have the same name and
# show how Python differentiates between them.

#In Python ,variables have a scope that determines where they can be accessed from.
#A variable's scope is the region of the program where it is defined and can be used.
#The variable created above the user defined function is considered as the global variable,
#whereas the variable created inside or within the function is considered as local variable.
#The print command inside the function will return the local variable.
#The print command after the function call will return the Global variable.

# Global variable
# a= 100
#
# def display():
#     # Local variable with the same name
#     a = 25
#     print("Inside the function, local a:", a)
#
# # Call the function
# display()
#
# # Print the global variable
# print("Outside the function, global a:", a)


# 5.	Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
#
# def calculate_area(length, width=5):
#     area = length * width
#     return area
#
# # Calling the function with both length and width
# area_length_width = calculate_area(15, 6)
# print("Area with length 15 and width 6:", area_length_width)
#
# # Calling the function with only length
# area_with_default_width = calculate_area(15)
# print("Area with length 15 and default width 5:", area_with_default_width)

#For calculating the area length and width are required.
#In the user defined function calculate_area length and width are to be given while
# defining the function.Here width =5 is given as default argument.
#While calling the function with both length and width,both arguments are given and the
#area is printed.
#If only the value for length is given then the value for the width will be taken by the
#interpreter is the default argument.Thus, the area is calculated in the second case.



