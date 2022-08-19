expect_date=int(input("enter the expect_date"))
expect_month=int(input("enter the expect_month"))
expect_year=int(input("enter the expect_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if return_date<=expect_date and expect_month==return_month and expect_year==return_year:
    print("cost of book",0)
elif return_date>=expect_date and expect_month==return_month and expect_year==return_year:
    a=return_date-expect_date
    b=a*15
    print("cost of book",b)
elif return_month>=expect_month and expect_date==return_date and expect_year==return_year:
    x=return_month-expect_month
    y=x*500
    print("cost of book",y)
elif return_year>=expect_year:
    print("cost of book",10000)
else:
    print("invalid condition")