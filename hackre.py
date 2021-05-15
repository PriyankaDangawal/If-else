# without use split function do split question.


# # def name(a):
#     i=0
#     word=str(a)
#     while i<len(a):
#         print(word[i],end=" ")
#         i=i+1
# name("priyanka dangwal")

def timeConversion(s):
    if(s[-2:]=="AM" and s[:2]=='12'):
        return "00"+s[2:8+"AM"]
    elif(s[-2:]=='AM'):
        return s[0:8+"AM"]
    elif(s[-2:]=='PM' and s[:2]=='12'):
        return s[0:8+"PM"]
    else:
        return str(int(s[:2])+12)+s[2:8]+"PM"

s=input("enter the TIME:")
print(timeConversion(s))
