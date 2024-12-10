"""
Practical Example 6:
Write a Python program to check if a number is prime using if_else. 
"""
count=0
num=int(input("Enter the number := "))
for i in range(2,num):
    if num%i==0:
        count+=1
if count == 0:
    print(f"{num}is a prime number")
else:
    print(f"{num}is not a prime number")