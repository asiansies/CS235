# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #6: Generalized CRT, Data Structures, and More Isomorphisms

from math import floor
from fractions import gcd
from random import randint

'''
Problem 1.
a. 12 * x = 16 (mod 32) 
		16(mod 32) = {...16, 48...}
	12 * x = 48 (mod 32)
	12 * x = 12 * 4 (mod 32)
	x = 4 (mod 32)
	x = 4 + 32Z

b. x = 7 (mod 21)
   x = 21 (mod 49) 
   NO SOLUTION: Any number that is 21 (mod 49) would be 0(mod 21), not 7.

c. 2 * x = 12 (mod 26)
   2 * x = 2 * 6 (mod 26)
	x = 6 (mod 26)
	x = 6 + 26Z

d. x = 11 (mod 14)
   x = 18 (mod 21)

	a = b (mod (gcd(n,m)))
	11 = 18 (mod 7)
	11 = 4 (mod 7)
	This implies there is a solution:

		gcd(14, 21) = 7 and 11 = 4 (mod 7)

		x - 11 = 0 (mod 14)
		x - 11 = 7 (mod 21)

		x - 11 / 7 = 0 (mod 1)
		x - 11 / 7 = 1 (mod 3)

		x - 11 / 7 = 0 * 3 * 3 - inverse(mod 1) + (1 * 1 * 1 - inverse(mod 3))
		x - 11 / 7 = 0 + 1 * 1 - inverse(mod 3)
		x - 11 / 7 = 4
		x = 39

		14 * 21 / gcd(14, 21) = 42

		SOLUTION: x = 39 (mod 42)

e. x = 10 (mod 12)
   x = 2 (mod 16)

	a = b (mod (gcd(n,m)))
	10 = 2 (mod 4)
	This implies there is a solution:

		gcd(12, 16) = 4 and 2 = 10 (mod 4)

		x - 2 ≡ 0 (mod 16)
		x - 2 ≡ 8 (mod 12)

		x - 2 / 4 = 0 (mod 4)
		x - 2 / 4 = 2 (mod 3)

		x - 2 / 4 = 2 * 4 * 4 - inverse(mod 3) + (0 * 3 * 3 - inverse(mod 4))

		4 - inverse(mod 3) = 1

		x - 2 / 4 = 2 * 4 * 4
		x = 130

		12 * 16 / gcd(16,12) = 48
		x = 130 (mod 48) 

		SOLUTION: x = 34 (mod 48)

f. x^2 = 4 (mod 35)
   3 * x = 15 (mod 21)


Problem 2.
a. x = 14 (mod 16)
   x = 6 (mod 12)

	gcd(16,12) = 4 and since 14 = 6 (mod 4), there exists a solution:

		x - 14 = 0 (mod 16)
		x - 14 = 4 (mod 12)

		x - 14 / 4 = 0 (mod 4)
		x - 14 / 4 = 1 (mod 3)

		x - 14 / 4 = 0 * 3 * 3 - inverse(mod 4) + (1 * 4 * 4 - inverse(mod 3))
		x - 14 / 4 = 0 + 4 * 4 - inverse(mod 3)

		4 - inverse (mod 3) = 4

		x - 14 / 4 = 0 + 4 * 4
		x - 14 / 4 = 16

		x = 78
		x = 78 (mod 48)
		x = 30 (mode 48)

		SOLUTION: 30 hours have past since the alarm rang exactly at midnight. 
				  It is now 6AM.

b.

c.
'''

# Problem 3.
# a.
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
return (s, t)

def inv(a, m):
    (s,t) = egcd(a, m)
    return s % m if gcd(a,m) == 1 else None

def solveOne(c, a, m):
    i = inv(c, m)
    return (i * a) % m if not i is None else None

b.
def solveTwo(e1, e2):
    (c, a, m) = e1
    (d, b, n) = e2
    a = solveOne(c, a, m)
    b = solveOne(d, b, n)
    (s, t) = egcd(m, n)
    return (a*t*n + b*s*m) % (m*n)

c.
def solveAll(es):
    while len(es) > 1:
        (c, a, m) = es[0]
        (d, b, n) = es[1]
        s = solveTwo((c, a, m), (d, b, n))
        es = [(1, s, n*m)] + es[2:]
    return es[0][1] % es[0][2]

