import datetime

def cal_age(year,month,day):
    today = datetime.date.today()
    dob = datetime.date(year,month,day)
    age = (today-dob).days
    # return age
    print(age,"Days")

Y=int(input("Enter the Year:"))
M=int(input("Enter the Month:"))
D=int(input("Enter the Day:"))

cal_age(Y,M,D)

# user_input=input("Enter Your Date Of Birth in YYYY/MM/DD Formate:")
# dob=user_input.split('/')
# year,month,day=int(dob[0]),int(dob[1]),int(dob[2])
# your_age=cal_age(day,month,year)
# print(your_age)