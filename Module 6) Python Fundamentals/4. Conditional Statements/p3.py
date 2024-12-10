"""
Practical Example 7:
Write a Python program to calculate grades based on percentage using 
if-else ladder. 
"""
percentage = float(input("Enter the percentage := "))

if percentage >=80 and percentage<=100:
    grade = 'A'
elif percentage >=70 and percentage <=80:
    grade = 'B'
elif percentage >=50 and percentage <=70:
    grade = 'C'
else:
    grade = 'FAIL'
print(f"the grade for the percentage {percentage}% is: {grade}")