# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #3: Multiplicative Inverses, CRT, and Efficient Computation

from math import floor
from fractions import gcd

'''
Problem 1.
a. 8 * x = 2 (mod 5)
	gcd(8,5) = 1 so we can apply the theorem:
		= 8 * x = 2 (mod 5)
		= 8 * x = 8 * 4 (mod 5)
		= x = 4 (mod 5)
		= x = 4

b. Solve for x in Z/35Z
	x = 1 (mod 7)	=	1 + 7Z
	x = 3 (mod 5)	=	3 + 5Z

	= 5^(7-1) = 1 (mod 7)
	= 5^(7-1) * 5^-1 = 5^-1
	= 5^(7-2) = 5^-1
	= 5^5 = 5^-1
	= 125 = 5^-1
	= x * 5 = 1(mod7)
	= 1 + 7Z = {1,8,15,...}
	= 5x = 3 * 5
	= x = 3
	= 3 = 5^-1
	= 5 * y = 1 (mod 7)
    = 5 * y = 1(3 * 5)(mod 7)

	y = 43 (mod 7)
	y = 43

	x = 5 * y (mod 35)
	x = 5 * 3
	x = 15

	x = 43 (mod 35)
	x = 43

c. 	x = 2 (mod p)
	x = 4 (mod q)

	x1 = 2(mod p)
	x1 = 0(mod q)
	x2 = 0(mod p)
	x2 = 4(mod q)

	x1 + x2 = x1 + 0 (mod p) = a (mod p) = 2 (mod p)
	x1 + x2 = 0 + x2 (mod q) = b (mod q) = 4 (mod q)

	x1 = a * q * q^-1 (mod(p * q))
	x2 = b * p * p^-1 (mod(p * 1)) 

d.	x = 3 (mod 5)
	x = 6 (mod 14)
		
	3 + 5Z = {...8, 13, 18, 23, 28,...}
	6 + 14Z = {...20, 34, 48,...}
	x = 48


'''

# Problem 2.
def invPrime(a, p):
	if a == 0:
		return None
	return pow(a, p - 2, p)

def egcd(a, b):
	if a == 0:
		x = (b,0,1)
		return x
	else:
		z, y, x = egcd(b % a, a)
		result = (z, x - (b // a) * y, y)
		return result


def inv(a, m):
	z, x, y = egcd(a, m)
    
	if z != 1:
		return None
	if z == 1:
		return x % m

# Problem 3.
# Part a.
def solveOne(c, a, m):
	if gcd(c, m) == 1:
		for x in range(0, m):
			#if (c * x) % m == a:
			if pow(c * x, 1, m) == a:
			#if invPrime(c, m) == a:
				return x
	return None

# Part b.
def solveTwo(e1, e2):
	if solveOne(e1[0], e1[1], e1[2]) == None:
		return None

	if solveOne(e2[0], e2[1], e2[2]) == None:
		return None

	if gcd(e1[2], e2[2]) == 1:
		for x in range(0, e1[2]*e2[2]):
			if x % e1[2] == solveOne(e1[0], e1[1], e1[2]) and x % e2[2] == solveOne(e2[0], e2[1], e2[2]):
				return x
	return None

# Part c.
def solveAll(es):
	while len(es) > 1:
		Ci = es[0]
		Cj = es[1]
		x = solveTwo(Ci, Cj)
		Ck = (1, x, Ci[2] * Cj[2])
		es = es[2:]
		es.append(Ck)
	return es[0][1]

# Problem 4.
# Part a.
def sumOfPowers (nes, ps):
	k = 0
	list = []

	for p in ps: 
		for n in nes:
			k += pow(n[0], n[1], p)   
		list.append((k, 1, p))
		k = 0
          
	return solveAll(list)
	#return sum(pow(nes[x][0], nes[x][1]) for x in range(0,len(nes)))