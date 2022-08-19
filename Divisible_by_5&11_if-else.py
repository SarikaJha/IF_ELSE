varx=int(input("enter the number"))
if varx%5==0:
    if varx%11==0:
        print("divisible by 5 and 11")
    else:
        print("divisible by 5")
else:
    print("not divisible by 5 and 11")