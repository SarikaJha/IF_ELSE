user=int(input("enter the number"))    
if user%5==0:
    if user%11==0:
        print("divisible by 5 and 11")
    else:
        print("divisible by 5")
else:
    print("not divisible")