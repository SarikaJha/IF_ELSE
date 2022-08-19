expect_date=int(input("enter the expect_date"))
expect_month=int(input("enter the expect_month"))
expect_year=int(input("enter the expect_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if expect_year==return_year:
    if expect_month==return_month:
        if expect_date==return_date:
            print("no fine ")
        else:
            print("cost of book",(return_date-expect_date)*15)
    else:
        print("cost of book",(return_month-expect_month)*500)
else:
    print("cost of book",(return_year-expect_year)*10,000)