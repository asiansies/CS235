# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #5: Algebraic Structures and Isomorphisms

from math import floor
from fractions import gcd
from random import randint
from urllib.request import urlopen

'''
Problem 1.
a. [1,2,3,0] o [3,0,1,2]
	= [0,1,2,3]

b. [46,47,...,99,0,1,2,3,4,...,45]o[11,12,...,99,0,1,2,3,4,...,10]
	[46,47,...,99,0,1,2,3,4,...,45] = 46 E Z/100Z
	[11,12,...,99,0,1,2,3,4,...,10] = 11 E Z/100Z

	46 + 11 = 57
	[46,47,...,99,0,1,2,3,4,...,45]o[11,12,...,99,0,1,2,3,4,...,10]
	= [57,58,...,99,0,1,2,...,56]

c. p o q o p^-1 o q^-1
	p = [1,2,0]		q = [2,0,1]
	[1,2,0] o [2,0,1] o [0,2,1] o [1,0,2]
	= [1,2,0]

	p o q o p^-1 o q^-1
	= p

d. p o p o p o p
	= [0,1,2,...,n - 1]

e.          S_2			  |	  Z/4Z
  ====================================
   [1,3] o [1,3] = [1,3]  |	1 * 1 = 1
   [1,3] o [3,1] = [3,1]  |	1 * 3 = 3
   [3,1] o [1,3] = [3,1]  |	3 * 1 = 3
   [3,1] o [3,1] = [1,3]  |	3 * 3 = 1
  ====================================

f.  closure({3 + 9Z}, +)  |	  Z/3Z
  ====================================
	1				  = 1 |	0 + 0 = 0
	1+1			  	  =	2 |	0 + 1 = 1
	1+1+1			  =	0 |	0 + 2 = 2
	1+1+1+1			  =	1 |	1 + 0 = 1
	1+1+1+1+1		  =	2 |	1 + 1 = 2
	1+1+1+1+1+1		  =	0 |	1 + 2 = 0
	1+1+1+1+1+1+1	  =	1 |	2 + 0 = 2
	1+1+1+1+1+1+1+1	  =	2 |	2 + 1 = 0
	1+1+1+1+1+1+1+1+1 =	0 |	2 + 2 = 1
  ====================================

g.  closure({2 + 15Z}, *) |	  Z/4Z
  ====================================
	2				  = 2 |	1 + 1 = 2
	2*2			  	  =	4 |	1 + 3 = 4
	2*2*2			  =	8 |	3 + 1 = 4
	2*2*2*2			  =	1 |	3 + 3 = 2
  ====================================

h. There can be no isomorphism between the two algebraic structures 
   (S_4) and (Z/5Z, +) because Z/5Z contains 5 elements while (S_4)
   is a set of 4 elements -- they are not the same size.

'''

# Problem 2.
# a.
def permute(p, l):
	s = []
	for x in range(len(p)):
		s.append(l[p[x]])
	return s

# b.
def C(k, m):
	s = [x for x in range(0, m)]
	s2 = []
	for x in range(0, m):
		s2.append(s[(x + k) % m])
	return s2

# c.
def M(a, m):
	return [(a * x) % m for x in range(m)]

# d.
def sort(l):
	for x in range(len(l)): 
		s = C(x, len(l))
		if (sortAscend(permute(s, l)) == True):
			return s

	for x in range(1, len(l)):
		s2 = M(x,(len(l)))
		if (sortAscend(permute(s2, l)) == True):
			return s2

	return None

def sortAscend(l):
	for x in range(len(l)):
		if (x != 0):
			if (l[x] < l[x - 1]):
				return False
	return True

# Problem 3.
def unreliableUntrustedProduct(xs, n):
	url = 'http://cs-people.bu.edu/lapets/235/unreliable.php'
	return int(urlopen(url+"?n="+str(n)+"&data="+",".join([str(x) for x in xs])).read().decode())

# a. 
def egcd(a, b):
	(x, s, y, t) = (0, 1, 1, 0) 
	while b != 0:
		k = a // b
		(a, b) = (b, a % b)
		(x, s, y, t) = (s - k*x, x, t - k*y, y)
	return (s, t)

def privateProduct(xs, p, q):
	n = p * q
	phi_n = (p - 1) * (q - 1)
	e = 3
	inv_e = (egcd(e, phi_n)[0])
	while (inv_e < 0):
		inv_e = inv_e + phi_n
	s = [pow(xs[x], e, n) for x in range(len(xs))]         
	prod = unreliableUntrustedProduct(set, n)
	return pow(prod, inv_e, p)

# b.
def solveTwo(e1, e2):
	(c, a, m) = e1
	(d, b, n) = e2
	a = solveOne(c, a, m)
	b = solveOne(d, b, n)
	(s, t) = egcd(m, n)
	return (a*t*n + b*s*m) % (m*n)

def validPrivateProduct(xs, p, q):
	n = p * q
	phi_n = (p - 1) * (q - 1)
	e = 3
	rand = randint(1, q - 1)
	d = 0

	while (d % q != pow(rand, len(xs), q)):
		s = [solveTwo((1, xs[i], p), (1, rand, q)) for i in range(len(xs))]
		encrypt_set = [pow(s[x], e, n) for x in range(len(s))]
		c = unreliableUntrustedProduct(encrypt_set, n)
		inv_e = (egcd(e, phi_n)[0])

		while (inv_e < 0):
			inv_e = inv_e + phi_n

		c = pow(c, inv_e, p)
		d = solveTwo((1, c, q), (1, c, p))
	return d