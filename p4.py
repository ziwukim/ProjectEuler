from palchecker import *

max = 0
for i in range(1000):	# This is not two-digit's multiplication
	for j in range(1000):
		prod = i*j
		if palchecker(prod):
			if prod > max:
				max = prod
print (max)
