cost=int(input("enter the cost price"))
sale=int(input("enter the sale price"))
if cost>sale:
    if sale<cost:
        amount=sale-cost
        print("total loss amount=",amount)
elif sale>cost:
    if cost<sale:
        amount=cost-sale
        print("total profit amount=",amount)
else:
    print("no profit no loss")