import csv
import json
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
with open('organizer.json') as json_data:
	data = json.load(json_data)
	
orgName = data['name']
#orgEmail = data['email']
openTimes = [data['openMonday'], data['openTuesday'], data['openWednesday'], data['openThursday'], data['openFriday'], data['openSaturday'], data['openSunday']]
closeTimes = [data['closeMonday'], data['closeTuesday'], data['closeWednesday'], data['closeThursday'], data['closeFriday'], data['closeSaturday'], data['closeSunday']]
employeeType = data['employeeType']
timeInterval = 8 if employeeType == 'fulltime' else 5
timeleft = list()
sum_of_open_time = list()

def strToFloat(arr):
	return float(arr.split(":")[0]) + float(arr.split(":")[1]/60)

# TOTAL HOURS OPEN IN A WEEK
for i in range(7):
	timeleft.append([openTimes[i], closeTimes[i]])
	open_time = strToFloat(openTimes[i])
	close_time = strToFloat(closeTimes[i])
	sum_of_open_time.append(close_time - open_time)

csv_name = "new_file.csv"
f = open(csv_name, 'r')
reader = csv.reader(f, delimiter=',')

users = list()
rows = [r for r in reader]
employee_count = int(len(rows)/4)+1
if employee_count >= 10:
	for row in range(0, len(rows), 2):
		times = []
		row_data = rows[row]
		if row % 4 == 0:
			tmp_user = dict()
			name = row_data[0]
			tmp_user["name"] = name
			tmp_user["daysWorked"] = 0
		else:
			timesO = row_data
			for timeN in range(0, len(timesO)-1, 2):
					times.append([timesO[timeN], timesO[timeN+1]])
			tmp_user["time"] = times
			users.append(tmp_user)

for day in range(7):
	# sort employees based on start time
	users.sort(key=lambda x: x['time'][day][0].split(':')[0])
	empStartHour = 
#user['time'] = [[startMonday,endMonday],[startTuesday, EndTuesday], ...]
# for day in range(7):
# 	users.sort(key=lambda x: x['time'][day][0].split(':')[0])
# 	for user in users:
# 		#MAKING SURE THE USER HASN'T WORKED MORE THAN 5 DAYS
# 		if user['daysWorked'] < 5:
# 			#THE HOURS THAT THIS EMPLOYEE IS AVAILABLE TODAY
			# empStartHour = int(user['time'][day][0].split(':')[0])
			# empStartMinute = int(user['time'][day][0].split(':')[1])
			# empEndHour = int(user['time'][day][1].split(':')[0])
			# empEndMinute = int(user['time'][day][1].split(':')[1])
# 			#THE HOURS THAT ARE LEFT UNFILLED TODAY
# 			leftStartHour = int(timeleft[day][0].split(':')[0])
# 			leftStartMinute = int(timeleft[day][0].split(':')[1])
# 			leftEndHour = int(timeleft[day][1].split(':')[0])
# 			leftEndMinute = int(timeleft[day][1].split(':')[1])
# 			#checking start time
# 			#IF THE EMPLOYEE IS AVAILABLE BEFORE THE EARLIEST AVIALBLE TIME OF THE DAY OR EXACTLY AT IT
# 			if empStartHour < leftStartHour or user['time'][day][0] == timeleft[day][0]:
# 				empStartTime = timeleft[day][0]
# 			#CHECKING IF THE EMPLOYEE IS AVAILABLE AT THE EARLIEST HOUR LEFT BUT HAS A DIFFERENT MINUTE AVAILABLE TIME
# 			elif empStartHour == leftStartHour and empStartMinute != leftStartMinute:
# 				#THE EMPLOYEE WILL START AT THAT HOUR AND THE HIGHER MINUTE
# 				empStartTime = empStartHour+':'+ (empStartMinute if empStartMinute > leftStartMinute else leftStartMinute)
# 			#CHECHING IF THE EMPLOYEES STARTING AVAILABLE TIME IS MORE THAN THE EARLIEST START TIME BUT LOWER THAN THE LATEST END TIME
# 			elif empStartHour > leftStartHour and empStartHour < leftEndHour:
# 				#WE WILL SET THE EMPLOYEE TO START AT THE SOONEST POSSIBLE TIME
# 				empStartTime = user['time'][day][0]
# 			#CHECKING IF the last available hour is more than the 8 hour working mark of the employee
# 			#IF IT IS, THE EMPLOYEE WIL STOP WORKING AFTER 8 HOURS
# 			#IF IT IS NOT, THE EMPLOYEE WIL STOP WORKING AT THE LAST AVAILABLE HOUR
# 			empEndShift = str(empStartHour+8)+':'+empStartTime.split(':')[1] if leftEndHour > empStartHour+8 else timeleft[day][1]
# 			#Updating the left time
# 			timeleft[day][0] = empEndShift
	
# define sum of 
