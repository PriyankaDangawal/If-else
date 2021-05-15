num=int(input("enter the number"))
if num%3==0 and num%2!=0:
    print(1)
elif num%3==0 and num%2==0:
    print(0)
else:
    print(-1)