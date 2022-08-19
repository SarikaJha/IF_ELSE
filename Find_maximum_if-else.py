a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
# if a>b:
#     if a>c:
#         print(a,"a is maximum")
#     elif b>a:
#         print(b,"b is maximum")
#     else:
#         print(c,"c is maximum")
# elif b>a:
#     if b>c:
#         print(b,"b is maximum")
#     elif c>b:
#         print(c,"c is maximum")
#     else:
#         print(a,"a is maximum")
# elif c>a:
#     if c>b:
#         print(c,"c is maximum")
#     elif a>c:
#         print(a,"a is maximum")
#     else:
#         print(b,"b is maximum")
# else:
#     print("invalid condition")

if a>b and a>c:
    print(a,"a is maximum")
elif b>a and b>c:
    print(b,"b is maximum")
else:
    print(c,"c is maximum")