# Write a Python program to create a calculator using functions
def addition():
    num=int(input("Enter the number "))
    num2=int(input("Enter the number "))
    ans=num+num2
    print(f"addition of {num} and {num2} is {ans}")
def subtraction():
    num=int(input("Enter the number "))
    num2=int(input("Enter the number "))
    ans=num-num2
    print(f"Subtraction of {num} and {num2} is {ans}")
def multiplication():
    num=int(input("Enter the number "))
    num2=int(input("Enter the number "))
    ans=num*num2
    print(f"Multiplication of {num} and {num2} is {ans}")
def division():
    num=int(input("Enter the number "))
    num2=int(input("Enter the number "))
    ans=num//num2
    print(f"division of {num} and {num2} is {ans}")

print(" press 1 for addition of 2 number :")
print("  press 2 for subtracton of 2 number: ")
print(" press 3 for multiplication of 2 number : :")
print(" press 4 for divison  of 2 number : :")
choice=int(input("Enter the number :"))

if choice==1:
    print("------------------------------------------------------------------------")
    print("Addition ")
    addition()


elif choice==2:
    print("------------------------------------------------------------------------")
    print("subtraction ")
    subtraction()

elif choice==3:
    print("------------------------------------------------------------------------")
    print("multiplication ")
    multiplication()
    
elif choice==4:
    print("------------------------------------------------------------------------")
    print("division ")
    division()
