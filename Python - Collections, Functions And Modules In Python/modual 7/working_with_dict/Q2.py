# Write a Python program to merge two lists into one dictionary using a loop.
dict1={
    0:"age",
    1:"name",
    2:"Subject"
}
dict2={
    0:21,
    1:"bhatt Om",
    2:"Python"
    
    }
dict3={}
for i in range(len(dict1)):
    dict3[dict1[i]]=dict2[i]
print(dict3)