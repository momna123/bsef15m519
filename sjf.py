#!user/bin/python
def SJF(jobs, index):
    newjobs = list()
    elem = jobs[index]
    l = len(jobs)
    c = 0
    for i in range(l):
        o = jobs[i]
        if o < elem or (o == elem and i <= index):
            newjobs.append(o)
            c += 1
    return reduce(lambda x, y: x+y, newjobs[0:c])
    
SJF([3,10,20,1,2], 0) == 6
