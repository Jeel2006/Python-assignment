"""
Write a Python program that manipulates and prints strings using various string methods.

"""
str="hello world!"
str1 = "Hello World!"
str2 = "HELLO WORLD!"

# Using various string methods 
print("Original string=", str1)

#length
print("length of string=",len(str1))

#Converting to uppercase
print("Uppercase string=",str1.upper()) 

#Converting to lowercase

print("lowercase string=",str2.lower())

#count()
print("count a world=",str1.count("l"))

#title()
print("title=",str1.title())

#istitle 
print("istitle=",str1.istitle())
print("istitle=",str2.istitle())

#isupper
print("isupper=",str1.isupper())
print("isupper=",str2.isupper())

#islower
print("isupper=",str.isupper())
print("isupper=",str2.isupper())

#find
print("find=",str1.find("h"))
print("find=",str1.find("H"))

#rfind
print("rfind=",str.rfind("l"))
print("rfind=",str1.rfind("E"))

#replace    
print("replace=",str.replace('HELLO','world'))

#index
print("index=",str1.index('l'))

#rindex
print("rindex=",str.rindex('l'))

#strip
print("strip=",str.strip())

#lstrip
print("lstrip=",str.lstrip())

#rstrip
print("rstrip=",str.rstrip())

#split
print("split=",str1.split())

#isalpha
str1_1 ="helloworld"
print("isalpha=",str1_1.isalpha()) 
print("isalpha=",str1.isalpha()) 

#isalnum
str_2 = "Helloworld11"
print("isalnum=",str_2.isalnum())
print("isalnum=",str1.isalnum())

#isdecimal
decimal = "12345678910"
print("isdecimal=",decimal.isdecimal())
print("isdecimal=",str1.isdecimal())

#isdigit
print("isdigit=",decimal.isdigit())
print("isdigit=",str1.isdecimal())

