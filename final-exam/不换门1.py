import random
from numpy import *

m=[]
n=int(raw_input("please input the number of the cars: " ))

l=0.0

pick1 = raw_input("please choose one of the doors: ")
pick1 = int(pick1)

for i in range(10000):

    m=[]
    while n!=len(m):
        x=random.randint(1,10)
        if x in m:
            continue
        else:
            m.append(x)

    while 1:
	kick1 = random.randint(1,10)
        kick1=int(kick1)

        if kick1 not in m and kick1 != pick1:

	    pick2 = int(pick1)
            if pick2 in m:
        	l=l+1
		break
	    else:
		break

k=l/10000
print k
