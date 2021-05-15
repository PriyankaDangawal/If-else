n=int(input("enter the number"))
print(n)
if n==1:
    print("not prime number")
elif n>2:
    if n%3==0:
        print("not prime")
    else:
        print("prime number")
else:
    print("prime number")