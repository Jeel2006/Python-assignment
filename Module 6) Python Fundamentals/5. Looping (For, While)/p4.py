"""
Practical Example 4: Print this pattern using nested for loop: 
markdown 
Copy code 
* 
* * 
* * * 
* * * * 
* * * * *
"""
for row in range(1,6):
    for col in range(1,row+1):
        print(" * ",end="")
    print()
