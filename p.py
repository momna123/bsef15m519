#!user/bin/python
print ("priority schduling algorithm")
arrivalTime=[]
burstTime=0
pri=0

p1={1:[4,0,2],2:[2,3,4], 3:[1,5,5]}

for index in range(1,4):
	pri=p1.get(index)[0]
	print pri
	

print "gantt chart----"
totalTime=0
for i in range(1,4):
	print totalTime, "-----"
	burstTime=p1.get(i)[2]
	totalTime=totalTime+burstTime
print totalTime
