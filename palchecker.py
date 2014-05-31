from Deque import *

def palChecker(self, num):
	string = str(num)
	for i in len(string):
		d.addFront(string[i])

	flag = True
	while d.size() >=1 and flag == True:
		front = d.removeFront()
		rear = d.removeRear()
		if front != rear:
			flag = False
	
	return flag
