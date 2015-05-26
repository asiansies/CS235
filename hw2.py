# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #2: Modular Arithmetic, Random Numbers, and Primes

from fractions import gcd

'''
Problem 1.
a. 7 * x + 2 = 6 (mod 31)
	= 7 * x = 4 (mod 31)
	= 7 * x = 35 (mod 31)
	= 7 * x = 7 * 5 (mod 31)
	= x = 5 (mod 31)
	=> x = 5 + 31Z

b. 40 * x = 5 (mod 8)
	No solution. Not coprime. 

c. 3 * x + 1 = 1 (mod 3)
	= 3 * x = (mod 3)
	Since 3 = 0 (mod 3):
	0 * x = 0 (mod 3)
	Thus, any congruence class x in {0 + 3Z, 1 + 3Z, 2 + 3Z} is a solution
	to the equation.

d. 1 + 2 * x = 4 (mod 14)
	= 2 * x = 3 (mod 14)
	No solution. Any solution to 3 + 14Z will be an odd number, which is
	not divisble by 2. Therefore, x has no solution.

e. 17 * x * 11 = 300 (mod 389)
	= 17 * x = 289 (mod 389)
	= 17 * x = 17 * 17 (mod 389)
	= x = 17 (mod 389)
	=> x = 17 + 389Z

f. 718581210326212034673 * x = 1 (mod 9843578223646740201)
	No solution. No coprimes exist.

g. 48822616 * x = 14566081015752 (mod 3333333333333333333333333)
	=> 14566081015752 + 3333333333333333333333333Z
	= {3333333333347899414349085, 6666666666681232747682418, 10000000000014566081015751...}
	=> x = 298347 + 3333333333333333333333333Z
'''

# Problem 2.
def closest(t, ks):
	return min(ks, key = lambda x: abs(x - t))

# Problem 3a.
def findCoprime(m):
	for p in range(m//2, m - 1):
		if m % 2 == 1:
			return 2 ** p
		if gcd(p, m) == 1 & (m != p):
			return p

# Problem 3b.
def randByIndex(m ,i):
	for b in range(2, m - 1):
		if gcd(b, m) == 1:
			for k in range(1, m.bit_length()):
				a = closest((4/7 * m), [b ** k])
			return (a * i) % m

# Problem 4. 
def probablePrime(m):
	for k in range(1,100):
		a = randByIndex(m - 1, 2)
		if m % a == 0:
			return False
		if gcd(a, m) != 1:
			return False
		if (pow(a, (m-1), m) != 1):
			return False
	return True

# Problem 5.
def makePrime(d):
	n = randByIndex(((10 ** d) - 1), (2 ** (d//2) + 1))
	while probablePrime(n) == False:
		n = randByIndex(((10 ** d) - 1), (10 ** (d//2) + 1))
		return n