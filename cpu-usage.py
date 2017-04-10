#This program allows you to output your computer's current CPU usage in a readable format

#psutil is a library for retrieveing inormation about processes and system utilization
import psutil

#Every attribute of psutil represents seconds the CPU has spent in a given mode

#User is time spent by normal processes executing in user mode
userCPU = psutil.cpu_times().user

if userCPU < 60:
	print 'Time spent in normal processes: ', userCPU , 'sec'
else:
	print 'Time spent in normal processes: ', str(round(userCPU/60, 2)) , 'mins'


#Idle is time spent doing nothing 
idleCPU = psutil.cpu_times().idle

if idleCPU < 60:
	print 'Time spent doing nothing: ', idleCPU , 'sec'
else:
	print 'Time spent doing nothing: ', str(round(idleCPU/60, 2)) , 'mins'

#System is time spent by processes executing in kernel mode
systemCPU = psutil.cpu_times().system

if systemCPU < 60:
	print 'Time spent executing in kernel mode: ', systemCPU , 'sec'
else:
	print 'Time spent executing in kernel mode: ', str(round(systemCPU/60, 2)) , 'mins'


 
