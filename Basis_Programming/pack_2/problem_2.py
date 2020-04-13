def perfecto(x):
	sum = 1
	for i in range(2, int(x**0.5)+1):
		if x % i == 0:
			sum += i
			if i != x / i:
				sum += x / i
	if sum == x and x!=1:
		return('Perfect number')
	else:
		return ('Not perfect number')

a=int(input('Enter the number: '))
print(perfecto(a))
