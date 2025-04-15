"""  
Write a Python program to convert two lists into one
dictionary using a for loop.
"""
def convertdict(l1,l2):
    d3={}
    for i in range(len(l1)):
        d3[l1[i]]=l2[i]
    print(d3)
l1=["name","age","marks"]
l2=["Om",21,34]
print(convertdict(l1,l2))