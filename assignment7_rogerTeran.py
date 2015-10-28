# Assignment 7

with open('commuter_schedule.csv', 'r') as f:
    for line in f:
        print(line)

times = list()
with open('commuter_schedule.csv', 'r') as f:
    for line in f:
        line_list = line.split(',')
        times.append(line_list[1])
    print(times)

import datetime as dt

bus_travel_time = times[0]
hours,minutes,seconds = bus_travel_time.split(':')
x = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))
print(x)

train_travel_time = times[1]
hours,minutes,seconds = train_travel_time.split(':')
y = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))
print(y)

bus_schedule= [('#27','10:20:36'),('#42','10:35:23'),('#71','10:42:55'),('#84','11:33:21')]
train_schedule = [('#2','10:37:00'),('#4','11:05:00'),('#6','11:37:00')]

hours,minutes,seconds = bus_travel_time.split(':')
bus_timedelta = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))

hours,minutes,seconds = train_travel_time.split(':')
train_timedelta = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))

print(bus_timedelta,train_timedelta)

transportation_timetable = list()

for bus in bus_schedule:
    bus_scheduler = tuple()
    bus_number = "Bus " + bus[0]
    # print(bus_number)
    hours,minutes,seconds = bus[1].split(':')
    bus_departure = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))
    # print(bus_departure)
    bus_arrival = bus_departure + x
    # print(bus_arrival)
    bus_scheduler = (bus_number, bus_departure, bus_arrival)
    # print(bus_scheduler)
    transportation_timetable.append(bus_scheduler)

for train in train_schedule:
    train_scheduler = tuple()
    train_number = "Train " + train[0]
    # print(train_number)
    hours,minutes,seconds = train[1].split(':')
    train_departure = dt.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))
    # print(train_departure)
    train_arrival = train_departure + y
    # print(train_arrival)
    train_scheduler = (train_number, train_departure, train_arrival)
    # print(train_scheduler)
    transportation_timetable.append(train_scheduler)

print(transportation_timetable)

for transport in transportation_timetable:
    print(transport[0], str(transport[1]), str(transport[2]))

from operator import itemgetter
transportation_timetable.sort(key=itemgetter(2))
for transport in transportation_timetable:
    print(transport[0], str(transport[1]), str(transport[2]))

print("------------------------------------------")
print("----------THE ACTUAL ASSIGNMENT-----------")
print("------------------------------------------")
print("Question 1: ")
print("Which service will get there the earliest? " + transportation_timetable[0][0])

print("------------------------------------------")
print("Question 2: ")

from operator import itemgetter
transportation_timetable.sort(key=itemgetter(2))
for transport in transportation_timetable:
    if str(transport[2]) < "13:00:00":
        last_ride = transport[0]
    else:
        break
print("What service should the passenger take so that he/she can leave as late as possible but still arrive before 1pm? "+ last_ride)
