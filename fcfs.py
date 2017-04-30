#!user/bin/python
print ("hello welcome to python")
print ("first come first serve")
arrivalTime=[]
burstTime=0
#n=0

p1={1:[0,2],2:[3,4], 3:[5,5]}
for index in range(1,4):
	arrivalTime=p1.get(index)[0]
	#if(index==0):
	#	n=arrivalTime
	#if(n>arrivalTime):
	#	n=arrivalTime 
	print "ARRIVAL TIME ", arrivalTime
print "gantt chart----"
totalTime=0
#if(totalTime>0):
	#print "0 --- ",totalTime,"idel time"
for i in range(1,4):
	print totalTime, "-----"
	burstTime=p1.get(i)[1]
	totalTime=totalTime+burstTime
print totalTime
	
