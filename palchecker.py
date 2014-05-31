from Deque import *

def palchecker(num):
	string = str(num)
	d = Deque()
	for i in string:
		d.addFront(i)

	flag = True
	while d.size() > 1 and flag:
		front = d.removeFront()
		rear = d.removeRear()
		if front != rear:
			flag = False
	
	return flag
