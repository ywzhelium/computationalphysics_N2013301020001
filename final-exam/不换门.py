import random
from numpy import *

n=int(raw_input("please input the number of the doors: "))
a=range(1,n+1)

j=0.0

pick1 = raw_input("please choose one of the doors: ")
pick1 = int(pick1)

for i in range(1,10000 +1):

    from random import choice
    car = choice(a)

    while 1:
	  kick1 = choice(a)
          kick1=int(kick1)
	  if kick1 != car and kick1 != pick1:

		pick2 = int(pick1)
		if pick2 == car:
			j=j+1
			break
		else:
			break

k=j/10000
print k
