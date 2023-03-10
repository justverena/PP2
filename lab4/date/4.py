from datetime import date, datetime,timedelta,time
day2 = datetime.today()
day1 = datetime.strptime('2005 04 01 10:20:33', '%Y %m %d %H:%M:%S')
d = (day2 - day1).seconds
print(d)