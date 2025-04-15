#Write a Python program to update a value at a particular key in a dictionary.
student={
    "name":"om",
    "age":21 ,
    "subject":"python",
    "roll no": 9
}
print(student)
student["name"]="bhatt"
print(student)
print("----------------------------------")
student["roll no"]=10
print(student)
print("----------------------------------")
student["subject"]="java"
print(student)