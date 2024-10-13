"""Exercise 1
Name your file: MonthNames.py
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
An example run of the program (numbers in bold are typed in by the user)
Enter the month: 3
Month 3 is March"""

#MonthNames.py
#month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
 #      7:"July",8:"August",9:"September",10:"October",11:"November",
  #     12:"December"}
#month_number=int(input("Enter the month(1-12):"))
#i=month_number
#if i <= month_number <=12:
#       print(f"month{month_number}is {month[month_number]}")
#else:
 #      print("Please enter a number between 1 and 12")


"""
Exercise 2
A certain cinema currently sells tickets for a full price of 6 pounds, 
but always sells tickets for half price to people who are less than 16 years old,
 and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)
Enter your age: 63
Your ticket costs £2.00
"""
#full_price = 6.00
#age=int(input("Enter your age:"))
#if age < 16:
 #      ticket_price = full_price/2
#elif age >=60:
 #      ticket_price = full_price/3
#else:
 #      ticket_price = full_price

#print(f"Your ticket costs pound{ticket_price:2}")


"""
Exercise 3
Name your file: BodyMassIndex.py
Write a program to calculate your BMI and give weight status. Body Mass Index (BMI)
 is an internationally used measurement to check if you are a healthy weight for your 
 height.The metric BMI formula accepts weight in kilograms and height in meters:
BMI= weight(kg)/height2(m2)
BMI Weight Status Categories table
BMI range - kg/m2   Category
Below 18.5                    Underweight
18.5 -24.9         Normal
25 - 29.9          Overweight
30 & Above     Obese
An example run of the program (numbers in bold are typed in by the user)
Enter your weight in (kg): 75
Enter your height in (m): 1.70
Your BMI is: 25.95
You are in the “overweight” range.
"""
#BodyMassIndex.py
#def calculate_bmi(weight,height):
#    return weight/(height**2)

#def weight_status(bmi):
    #if bmi < 18.5:
     #   return "Underweight"
    #elif 18.5 <= bmi <24.9:
     #   return "Normal"
    #elif 25 <= bmi <29.9:
   #     return "Overweight"
  #  else:
 #       return "Obese"

#weight = float(input("Enter your wight in (kg):"))
#height = float(input("Enter your height in(m):"))
#bmi =calculate_bmi(weight,height)
#status =weight_status(bmi)

#print(f"Your BMI is:{bmi}")
#print(f"You are in the'{status}' range.")

"""
Exercise 4
Write a Python program to receive 3 numbers from the user and print 
the greatest among them
"""
#num1=int(input("Enter the first number:"))
#num2=int(input("Enter the second number:"))
#num3=int(input("Enter the third number:"))

#greatest= max(num1,num2,num3)
#print(f"The greatest number among {num1},{num2},& {num3},is{greatest}")


"""
Exercise 5
Find the factorial of a given number using loops(note the number is received from the user
"""
#def factorial(n):
#    result = 1
#    for i in range(1,n+1):
#        result *= i
#    return result

#number = int(input("Enter a number to calculate its factorial:"))

#if number < 0:
#    print("Factorial is not defined for negative numbers.")
#else:
#    fact = factorial(number)
#    print(f"The factorial of {number}is {fact}.")

"""
Exercise 6
Reverse a number using while loop
"""
#def reverse_number(n):
#    reversed_num = 0
#    while n > 0:
#        digit = n % 10
#        reversed_num = reversed_num *10 +digit
#        n //=10
#    return reversed_num

#number = int(input("Enter a number to reverse:"))
#reversed_number = reverse_number(number)
#print(f"The reversed number is: {reversed_number}")


"""
Exercise 7
Finding the multiples of a number using loop
"""
#def find_multiples(number,count):
#    multiples = []
#    for i in range(1,count+1):
#        multiples.append(number *i)
#    return multiples

#number =int(input("Enter a number to find its multiples:"))
#count = int(input("How many multiples do you want to find?:"))
#multiples = find_multiples(number,count)
#print(f"The first{count} multiples of {number} are:{multiples}")

"""Exercise 8
Write a program to print the inputted value as it is and break the loop if 
the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
Done"""
#while True:
#    msg =input(":")
#    if(msg == "done"):
#        print("Done")
#        break
#    else:
#        print(msg)

"""
Exercise 9
Write a program that prints the numbers from 1 to 10. But for multiples
    of three print "Fizz" instead of the number and for the multiple of five 
    print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
"""
#for i in range(1,11):
#    if i % 3 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)


"""
Exercise 10
Write a program to print the following pattern:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
#for i in range(5,0,-1):
#    for j in range(i,0,-1):
#        print(j,end ='')
#    print()
#########