"""
Write a Python program to demonstrate string slicing. 

"""

str1 = "Hello world!"

print("Original String: ",str1) #Slicing the string

print("slice from start to 5th character:",str1[:5]) # Slicing from the start to the 5th character

print("slice from 7th character to the end:",str1[7:]) # Slicing from the 7th character to the end

print("slice from 7th to 10th character :",str1[7:11]) # Slicing a substring from the 7th to the 11th character

print("Slice with positive indices:",str1[0:]) # Slicing with postive indices

print("Slice with negative indices (last 5 characters):",str1[-5:]) # Slicing with negative indices
 
print("Slice every 2nd character:", str1[::2]) # Slicing with a step value

print("Reversed string:", str1[::-1])# Reverse the string using slicing 