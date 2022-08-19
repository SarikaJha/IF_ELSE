day=input("enter the day")
meal=input("enter meal time")
if day=="monday":
    if meal=="breakfast":
        print("poori sabzi")
    elif meal=="lunch":
        print("sambhar rice")
    elif meal=="dinner":
        print("chicken rice")
    else:
        print("chawal")
elif day=="tuesday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma rice")       
    elif meal=="dinner":
        print("roti sabzi")
    else:
        print("rice")
else:
    print("anything")