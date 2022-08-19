council=input("enter the post")
name=input("enter the name")
if council=="disco":
    if name=="Rajeshwari" or name=="Worshimla":
        print("looking after students")
        print("discipline")
    else:
        print("No")
elif council=="T and P":
    if name=="Grace" or name=="Anisha":
        print("taking interview")
        print("taking care related to study")
    else:
        print("Others")
elif council=="IT":
    if name=="Suvarna":
        print("providing laptop")
        print("manage network")
    else:
        print("Any")
elif council=="O and C":
    if name=="Teresa":
        print("advitising Navgurukul")
        print("communicating ousider")
    else:
        print("anything")
elif council=="FC":  
    if name=="Seminao" or name=="Likitha":
        print("providing food")
        print("taking care related to food")
    else:
        print("nothing")
elif council=="FM":
    if name=="Onring" or name=="Chunkham":
        print("garbages")
        print("maintaining the campus")
    else:
        print("none")
elif council=="health cordinator":
    if name=="Karishma":
        print("providing medicine")
    else:
        print("error")
else:
    print("invalid condition")