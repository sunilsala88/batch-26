# import datetime

# d1=datetime.datetime(2024,7,20,14,55,1)
# print(d1)

# d01=datetime.date(2024,1,1)
# print(d01)

# t1=datetime.time(14, 55, 1)
# print(t1)

import datetime as dt
dt1=dt.datetime(2024,1,1)
print(dt1)

print(dt1.timestamp())

current_time=dt.datetime.now()
print(current_time)
print(current_time.timestamp())

t1=current_time.timestamp()

print(type(t1))
print(type(dt1))

st2='Feb-20 15:02:22 2024'
print(type(st2))

#convert string to datetime
f='%b-%d %H:%M:%S %Y'
datetime_object=dt.datetime.strptime(st2,f)
print(datetime_object)

#convert datetime to string
current_time=dt.datetime.now()
print(current_time)
print(type(current_time))
st3=current_time.strftime('%Y-%m-%d %H:%M:%S')
print(st3)
print(type(st3))


#convert datetime to int(epoch)
epoch=current_time.timestamp()
print(epoch)

#convert epoch (int) to datetime
epoch=1721468001
dt4=dt.datetime.fromtimestamp(epoch)
print(dt4)


#1721468001 to string
n=1721468001
#convet epoch to dt
dt1=dt.datetime.fromtimestamp(n)
#convert dt to str
st2=dt1.strftime('%Y/%m/%d')
print(st2)


import calendar

last_thur_2024=[]

for month in range(1,13):
    days=calendar.monthrange(2024, month)[1]
    last_day=dt.datetime(2024,month,days)    
    while True:
        if last_day.weekday()==3:
            break
        last_day=last_day-dt.timedelta(days=1)
    last_thur_2024.append(last_day)


print(last_thur_2024)

print(current_time)
day_1=dt.timedelta(seconds=1)
print(current_time+day_1)


d1=dt.date(2024,1,1)

t1=dt.time(10,10,10)

print(d1,t1)

dt1