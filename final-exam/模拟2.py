import random

door1 = 1
door2 = 2
door3 = 3
j=0.0

pick1 = raw_input("please choose one of the doors: ")
pick1 = int(pick1)

for i in range(10000):

    car = random.randint(1,3)

    while 1:
	  kick1 = random.randint(1,3)
	  kick1 = int(kick1)
	  if kick1 != car and kick1 != pick1:

                a=[1,2,3]
                a.remove(pick1)
                a.remove(kick1)
                pick2 = a[0]
		pick2 = int(pick2)

		if pick2 == car:
		    j=j+1
		    break
		else:
	            break

k=j/10000
print k
