"""
Exercise1
Write Python code that prints your name,student number and email address.
"""
#print('Bob,ST1001,bob@gmail.com')

"""
Exercise 2
Write a Python code that prints your name,student number and email address using
escape sequences
"""
#print('\tBob,\tST1001,\tbob@gmail.com')#\t tab sequence
#print('Bob,\nST1001,\nbob@gmail.com')#\n nextline sequence
#print('Bob,ST1001,\bbob@gmail.com')#\b back space sequence

"""
Exercise 3
Write Python code that add,subtract,multiply and divide the two numbers.
You can use the two numbers 14 and 7.
"""
#var1=int('14')
#var2=int('7')
#print((var1+var2),(var1-var2),(var1*var2),(var1/var2))

"""
Exercise 4
Write a Python code that displays the numbers from 1 to 5 as steps.
"""
#print('1\n2\n3\n4\n5')

"""
Exercise 5
Write a Python code that outputs the following sentence(including the quotation marks
and line break) to the screen:
An example runs of the program:
"SDK"stands for"Software Development Kit",
whereas
"IDE" stands for "Integrated Development Environment".
"""
#print("""\"SDK\"stands for\"Software Development Kit\",
#\nwhereas\n\"IDE\" stands for \"Integrated Development Environment\".\
""")

#"""
#Exercise 6
#Practice and check the output
#print("python is an \"awesome\" language".)
#print("python\n\t2023")
#print('I\'m from Entri.\b')
#print("\65")
#print("\x65")
#print("Entri","2023",sep="\n")
#print("Entri","2023",sep="\b")
#print("Entri","2023",sep="*",end="\b\b\b\b")
#"""

#print("python is an \"awesome\" language".)

#print("python\n\t2023")

#print('I\'m from Entri.\b')

#print("\65")

#print("\x65")

#print("Entri","2023",sep="\n")

#print("Entri","2023",sep="\b")

#print("Entri","2023",sep="*",end="\b\b\b\b")

"""
Exercise 7
Define the variables below.Print the types of each variable.
What is the sum of your variables?(hint:use a type conversion function.)
What datatype is the sum? num=23 textnum="57" decimal=98.3
"""
#num=23
#print(type(num))

#textnum=int("57")
#print(type(textnum))

#decimal=98.3
#print(type(decimal))
#sum=num+textnum+decimal
#print(sum)
#print(type(sum))

"""
Exercise 8
Calculate the number of minutes in a year using variables for each unit of time,
print a statement that describes what your code does also.Create three variables
to store no of days in a year,minute in an hour,hours in a day,then calculate
the total minutes in a year and print the values.(hint)total number of minutes
in an year=No.of days in an year*Hours in a day*Minutes in an hour."""

"""
hour=60 minutes
Day=24 hrs
Year=365 days
"""
#totalMinAnYear=365*24*60
#print(totalMinAnYear,"minutes in an year")

"""
Exercise 9
Write a Python code that asks the user to enter his/her name and then
 output/prints his /her name with a greeting."""
#name=input("Please enter your name:")
#print(f"Name of the candidate is{name}.Hi{name},welcome to Python programming")

""""
Exercise10
Name your file:PoundsToDollars.py
Write a program that asks the user to enter an amount in pounds.and the program
calculates and converts an amount in dollar($)"""

#amount=input("Please enter amount in pounds:")
#print(f"poundXXX are$XXX")
