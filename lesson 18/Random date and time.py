import random
import time

def getrandomdate(startdate, enddate):
    print("printing random date between ", startdate ," and the ", enddate)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"

    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))

    randomtime = starttime +randomgenerator * (endtime-starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))

    return randomdate

print("randome date = ", getrandomdate("1/1/2000", "12/31/2020"))
