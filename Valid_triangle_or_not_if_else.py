# a=int(input("enter the side"))
# b=int(input("enter the side"))
# c=int(input("enter the side"))
# if a!=0 and b!=0 and c!=0:
#     if a+b>=c and b+c>=a and c+a>=b:
#         print("valid triangle")
# else:
#     print("invalid triangle")

   ##SECOND METHOD

a=int(input("enter the first angle"))
b=int(input("enter the second angle"))
c=int(input("enter the third angle"))
if a+b+c==180:
    print("triangle is valid")
else:
    print("triangle is invalid")