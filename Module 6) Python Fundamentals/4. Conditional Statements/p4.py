"""
Practical Example 8:
Write a Python program to check if a person is eligible t
o donate blood 
using a nested if. 
"""
age = int(input("Enter your age := "))

if age>18 and age<60:
    blood = input("Enter your blood :=")
    if blood == 'A+':  
        print("You are eligible to donate blood.")
    elif blood == 'A':
        print("You are eligible to donate blood.")
    elif blood == 'B+':
        print("You are eligible to donate blood.")
    elif blood == 'B':
        print("You are eligible to donate blood.")
    elif blood == 'C+':
        print("You are eligible to donate blood.")
    elif blood == 'C':
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood.")
else:
    print("You are not eligible to donate blood.")