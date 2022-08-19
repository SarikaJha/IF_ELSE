x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
if x==y and x==z or y==x and y==z or z==x and z==y:
    print("equilateral")
elif x==y and x!=z or y==x and y!=z or z==x and z!=y:
    print("isosceles")
elif x!=y and x!=z or y!=x and y!=z or z!=x and z!=y:
    print("scalene")
else:
    print("invalid")