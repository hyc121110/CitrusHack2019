
from datetime import datetime
import time
import json
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
with open('organizer.json') as json_data:
	data = json.load(json_data)
	
orgName = data['name']
orgEmail = data['email']
openTimes = [data['openMonday'], data['openTuesday'], data['openWednesday'], data['openThursday'], data['openFriday'], data['openSaturday'], data['openSunday']]
closeTimes = [data['closeMonday'], data['closeTuesday'], data['closeWednesday'], data['closeThursday'], data['closeFriday'], data['closeSaturday'], data['closeSunday']]
timeleft = []
for day in range(7):
	timeleft.append([openTimes, closeTimes])

#users = [obj, obj, obj, ...]
#user.time = [[startMonday,endMonday],[startTuesday, EndTuesday], ...]
for day in range(7):
	for user in users :
		#MAKING SURE THE USER HASN'T WORKED MORE THAN 5 HOURS
		if user.daysWorked < 5:
			#THE HOURS THAT THIS EMPLOYEE IS ABAILABLE TODAY
			empStartHour = int(user.time[day][0].split(':')[0])
			empStartMinute = int(user.time[day][0].split(':')[1])
			empEndHour = int(user.time[day][1].split(':')[0])
			empEndMinute = int(user.time[day][1].split(':')[1])
			#THE HOURS THAT ARE LEFT UNFILLED TODAY
			leftStartHour = timeleft[day][0].split(':')[0]
			leftStartMinute = timeleft[day][0].split(':')[1]
			leftEndHour = timeleft[day][1].split(':')[0]
			leftEndMinute = timeleft[day][1].split(':')[1]
			#checking start time
			#IF THE EMPLOYEE IS AVAILABLE BEFORE THE EARLIEST AVIALBLE TIME OF THE DAY OR EXACTLY AT IT
			if empStartHour < leftStartHour || user.time[day][0] == timeleft[day][0]:
				empStartTime = timeleft[day][0]
			#CHECKING IF THE EMPLOYEE IS AVAILABLE AT THE EARLIEST HOUR LEFT BUT HAS A DIFFERENT MINUTE AVAILABLE TIME
			elif empStartHour == leftStartHour && empStartMinute != leftStartMinute:
				#THE EMPLOYEE WILL START AT THAT HOUR AND THE HIGHER MINUTE
				empStartTime = empStartHour+':'+ (empStartMinute if empStartMinute > leftStartMinute else leftStartMinute)
			#CHECHING IF THE EMPLOYEES STARTING AVAILABLE TIME IS MORE THAN THE EARLIEST START TIME BUT LOWER THAN THE LATEST END TIME
			elif empStartHour > leftStartHour && empStartHour < leftEndHour:
				#WE WILL SET THE EMPLOYEE TO START AT THE SOONEST POSSIBLE TIME
				empStartTime = user.time[day][0]
			#CHECKING IF the last available hour is more than the 8 hour working mark of the employee
			#IF IT IS, THE EMPLOYEE WIL STOP WORKING AFTER 8 HOURS
			#IF IT IS NOT, THE EMPLOYEE WIL STOP WORKING AT THE LAST AVAILABLE HOUR
			empEndShift = str(empStartHour+8)+':'+empStartTime.split(':')[1] if leftEndHour > empStartHour+8 else timeleft[day][1]
			#Updating the left time
			timeleft[day][0] = empEndShift
	