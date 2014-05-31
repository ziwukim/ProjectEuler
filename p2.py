num1 = 1
num2 = 2
sum = 2

num_fibo = num1 + num2
while num_fibo < 4000000:
#while num_fibo < 100:
	if num_fibo%2 == 0:
		sum += num_fibo
	num1, num2 = num2, num_fibo
	num_fibo = num1 + num2
print (sum)  
