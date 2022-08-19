age=int(input("enter the age"))
sex=input("enter sex:M or F")
marital_status=input("enter marital_status:Y or N")
if sex=="F":
    if marital_status=="Y":
        print("she will work only in urban areas")
    else:
        print("she is not allowed to work")
elif age>20 and age<40:
    if sex=="M":
        if marital_status=="Y":
            print("he may work anywhere")
        else:
            print("he won't work")
elif age>40 and age<60:
    if sex=="M":
        if marital_status=="Y":
            print("he will work in urban areas only")
        else:
            print("he can't work")
else:
    print("ERROR")
