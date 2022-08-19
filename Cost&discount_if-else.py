cost=int(input("enter the cost"))
if cost>1000:
    discount=(cost*10/100)
    print(cost-discount)
else:
    print("no discount")