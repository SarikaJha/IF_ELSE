language=input("enter the language")
if language=="english":
    print("Welcome to Punjab National Bank")
    balance=70000
    print("transaction:\n1.balance inquiry:\n2.withdraw:\n3.deposit:\n4.transfer money:\n5.exit")
    transaction=int(input("enter the transaction:"))
    if transaction==1 or transaction==2 or transaction==3 or transaction==4:
        atm_pin=int(input("enter the pin:"))
        if atm_pin==1800:
            if transaction==1:
                print("balance is",balance)
                print("collect your card\nThank you")
            elif transaction==2:
                withdraw_amount=int(input("enter the withdraw amount:"))
                if withdraw_amount<=balance:
                    total=balance-withdraw_amount
                    print(total)
                    print("collect your cash\nThank you")
                else:
                    print("you  have no balance")
            elif transaction==3:
                deposit=int(input("enter the deposit:"))
                if deposit>0:
                    total=balance+deposit
                    print(total)
                    print("your deposit is successful\nThank you")
                else:
                    print("no deposit")
            elif transaction==4:
                transfer_money=int(input("enter the transfer_money:"))
                if transfer_money>0:
                    total=balance-transfer_money
                    print(total)
                    print("your money has been transfer\nThank you")
                else:
                    print("transfer failed")
        else:
            print("wrong pin")
    elif transaction==5:
        exit=input("do you want exit?:")
        if exit=="yes":
            print("Thank you for visiting")
        else:
            print("choose your transaction")
else:
    print("language does not exist")