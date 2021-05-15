a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if c>a>b:
    print(a,"second greatest nuber")
elif c<a<b:
    print(a,"second greatest number")
elif c>b>a:
    print(b,"second greatest number")
elif c<b<a:
    print(b,"second greatest number")
elif b>c>a:
    print(c,"second greatest number")
elif b<c<a:
    print(c,"second greatest number")
else:
    print("somethink wrong please try again")