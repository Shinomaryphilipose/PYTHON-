# Exercise 1: (score : 1)
# Write a Python program to read a file and display its contents
#file1=open("C:\\Users\\sgkur\\PycharmProjects\\python_d36_ENTRI\\Sample.txt",'r')
#print(file1)
#
# Exercise 2: (score : 1)
# Write a Python program to copy the contents of one file to another file
# def copy_new_file(source, destination):
#     with open("C:\\Users\\sgkur\\PycharmProjects\\python_d36_ENTRI\\Sample.txt", 'r') as sourc_file:
#         with open("C:\\Users\\sgkur\\Desktop\\PythonFilehandling\\Hello.txt", 'w') as desti_file:
#             desti_file.write(sourc_file.read())
#
# # Example usage:
# source_file = 'Sample.txt'
# destination_file = 'Hello.txt'
# copy_new_file(source_file, destination_file)

# Exercise 3: (score : 2)
# Write a Python program to read the content of a file and count the total number of words in that file.
# with open("C:\\Users\\sgkur\\Desktop\\PythonFilehandling\\Hello.txt",'r') as file1:
#     data = file1.read()
#     print(data)
#     print(len(data.split()))
#
# Exercise 4: (score : 1)
# Write a Python program that prompts the user to input a string and converts it to an integer. Use
# try-except blocks to handle any exceptions that might occur
#
# A=input("the string which is to be converted to int")
# try:
#     B=int(A)
#     print(B,"the string converted to integer")
# except ValueError:
#     print("This string cannot be converted to integer")

# Exercise 5: (score : 1)
# Write a Python program that prompts the user to input a list of integers and raises an exception
# if any of the integers in the list are negative.

# def check_negative_integers():
#     try:
#         # Get input from the user and convert it to a list of integers
#         a = input("Enter a list of integers separated by spaces: ")
#         num_list = [int(x) for x in a.split()]
#
#         # Check if any number in the list is negative
#         for num in num_list:
#             if num < 0:
#                 raise ValueError(f"Negative number detected: {num}")
#
#         print("All numbers are positive.")
#
#     except ValueError as e:
#         print(f"Error: {e}")
#
#
# # Call the function to check the numbers
# check_negative_integers()

# Exercise 6: (score : 2)
# Write a Python program that prompts the user to input a list of integers and computes the
# average of those integers. Use try-except blocks to handle any exceptions that might occur.use
# the finally clause to print a message indicating that the program has finished running.

# def compute_average_integer():
#     try:
#         # Prompt the user to input a list of integers
#         a1= input("Enter a list of integers separated by spaces: ")
#
#         # Convert the input string into a list of integers
#         num_list = [int(x) for x in a1.split()]
#
#         # Ensure there is at least one number in the list
#         if len(num_list) == 0:
#             raise ValueError("The list cannot be empty.")
#
#         # Compute the average
#         average = sum(num_list) / len(num_list)
#         print(f"The average of the numbers is: {average}")
#
#     except ValueError as e:
#         # Handle errors for invalid input (e.g., non-integer values or empty list)
#         print(f"Error: {e}")
#
#     finally:
#         # This block will always run, regardless of whether an exception occurred
#         print("Program has finished running.")
#
#
# # Call the function to compute the average
# compute_average_integer()

# Exercise 7 : (score : 2)
# Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message
# if there is no exception occurred.
# def write_to_file():
#     try:
#         # Prompt the user for the filename
#         filename = input("Enter the filename: ")
#
#         # Open the file in write mode and write a string to it
#         with open("C:\\Users\\sgkur\\PycharmProjects\\python_d36_ENTRI\\Sample.txt", 'w') as file:
#             file.write("This is a sample string written to the file.")
#
#         # Print a welcome message if no exceptions occur
#         print(f"Hi welcome '{filename}' written successfully!")
#
#     except Exception as e:
#         # Handle any exceptions that occur (e.g., file permission issues)
#         print(f"Error: {e}")
#
#
# # Call the function to write to the file
# write_to_file()
