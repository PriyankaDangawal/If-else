# n=int(input("enter number"))
# a=n%10
# b=(n//10)%10
# c=(n//100)%10
# new_number=(a*100)+(b*10)+(c*1) 
# if n<1000:
#     print(new_number)
# else:
#     print("its no greater than 1000")

n=int(input("enter the number"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev-rem)
