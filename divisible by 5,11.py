num=int(input("enter the number"))
if num%5==0 and num%11==0:
    print(num,"divisable by 5 and 11")
elif num%5==0:
    print(num,"divisable by 5")
elif num%11==0:
    print(num,"divisable by 11")
else:
    print(num,"divisable by number accepcted 5 and 11")