from palchecker import *

max = 0
for i in range(100):
	for j in range(100):
		prod = i*j
		if palchecker(prod):
			if prod > max:
				max = prod
				print prod 
print (max)
