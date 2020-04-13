from math import factorial, sqrt, atan, cos

x = 0.1 
e = 1e-6

e1 = e / 1.41
e2 = e / 1.41
e3 = e / 0.25


for i in range(11):

	v0 = 1 + x
	v1 = 1.0 
	v = (1 + v0) / 2.0

	n = 0
	while abs(v - v1) > e2:
		v1  = v
		v = (v1 + v0 / v1) / 2.0
		n += 1
	v += 2.8 * x
  
	w = 1.5 * x + 0.2

	s1 = 0
	s2 = 0

	k = 0
	while v ** (2 * k) / factorial(2 * k) > e1: 
		k += 1
	for i in range(k + 1):
		s1 += (-1) ** i * v ** (2 * i) / factorial(2 * i)

	k = 0
	while w ** (2 * k + 1) / (2 * k + 1) > e3:
		k += 1
	for i in range(k + 1):
		s2 += (-1) ** i * w ** (2 * i + 1) / (2 * i + 1)

	print("x =", round(x, 2), "f* =", s1 * s2, "f =", cos(2.8 * x + sqrt(1 + x)) * atan(1.5 * x + 0.2))
	x += 0.01