year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
       print("leap year")
else:
    print("not leap year")
    
   ##SIMPLE

year=int(input("enter the year"))
if year%4==0:
    print("leap year")
else:
    print("not leap year")