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