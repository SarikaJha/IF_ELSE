a=int(input("enter the year:"))
b=int(input("enter the month:"))
c=int(input("enter the date:"))
if b>=1 or b<=12 and c>=1 or c<=31:
    print((c+1),"/",b,"/",a)
else:
    print("not valid")