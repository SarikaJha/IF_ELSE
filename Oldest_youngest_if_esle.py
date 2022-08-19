a=int(input("enter the first age"))
b=int(input("enter the second age"))
c=int(input("enter the second age"))
if a>b and a>c:
    print(a,"a is oldest")
elif b>a and b>c:
    print(b,"b is oldest")
elif c>a and c>b:
    print(c,"c is oldest")
if a<b and a<c:
    print(a,"a is youngest")
elif b<a and b<c:
    print(b,"b is youngest")
elif c<a and c<b:
    print(c,"c is youngest")
else:
    print("same age") 