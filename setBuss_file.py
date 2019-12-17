import sys
import time
import datetime
from datetime import date
from datetime import timedelta

n = 40
dow = 3
doy = 1
flag = 1

#try :
#    dateList = sys.argv[1]
#except Exception as err:
#    print err

with open('list_of_holiday.txt', 'r') as file:
    holidayList = file.read()
    

date = datetime.datetime(2019,12,31)

while (date.strftime("%Y%m") < "202006"):
    if date.strftime("%Y%m%d") == '20201231':
        break
    date += datetime.timedelta(days=1)
    datenew = date.strftime("%Y%m%d")
    
    #if sunday or saturday
    if dow == 0 or dow == 6 :
        flag = 0
    else:
        #if holiday in weekdays
        if datenew in holidayList:
            flag = 0
        else:
            flag = 1 
    
    print "trade_date -> [%s] | trade_flag [%s] | dayweek [%s]| dayYear [%s]"%(datenew, flag,dow, doy)
    

    dow += 1
    doy += 1
    if dow == 7:
        dow = 0

