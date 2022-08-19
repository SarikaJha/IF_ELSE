x=int(input("enter the first age:-"))
y=int(input("enter the second age:-"))
z=int(input("enter the third age:-"))
if x>y and y>z:
    print(x,"is oldest",y,"is younger",z,"is youngest")
elif y>z and z>x:
    print(y,"is oldest",z,"is younger",x,"is youngest")
elif z>x and x>y:
    print(z,"is oldest",x,"is younger",y,"is youngest") 
elif y>x and x>z:
    print(y,"is oldest",x,"is younger",z,"is youngest")
elif z>y and y>x:
    print(z,"is oldest",y,"is younger",x,"is youngest")
elif x>z and z>y:
    print(x,"is oldest",z,"is younger",y,"is youngest")
else:
    print("one or more number are equal")      