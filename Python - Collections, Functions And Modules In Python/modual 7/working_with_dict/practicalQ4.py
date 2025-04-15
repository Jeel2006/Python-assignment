#
def count_str(str):
    d={}
    for i in str:
        d[i]=str.count(i)
    return d
str=input("Enter the string :")
print(count_str(str))