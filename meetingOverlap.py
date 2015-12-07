#!/usr/bin/python
#save the dif and start time
def printme(x):
    #print x
    #print "time difference : ",x[1]-x[0]
    return x[1]-x[0]

def answer(x):
    counter=0
    max=0
    dif=0
    diff=[]
    start=[]
    print "size of list is :",len(x)
    for curlist in x:
        dif = printme(x[counter])
        diff.append(curlist[1]-curlist[0])
        start.append(curlist[0])
        print "current diff :", dif
        #print curlist[0],"",curlist[1]
        counter=counter+1

    for ii in range(0,counter): 
        print diff[ii],"",start[ii]
        #if dif==1 and start:
            #max=max+1
        #dif=0
    return max

mylist = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
mylist2 =[[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
myanswer = answer(mylist2)
print myanswer

