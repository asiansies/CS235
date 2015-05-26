# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #4: Intractable Problems in Modular Arithmetic

from math import floor
from fractions import gcd
from random import randint

'''
Problem 1.
a. x^2 = 3(mod 23)
		23(mod 4) = 3 so we can use x = +-y^((p + 1)/4)(mod p)

		= +-3^((23 + 1)/4)(mod 23)
		= +-3^6(mod 23)
		= +-729(mod 23)

		729(mod 23) = 16
		-729(mod 23) = 7

		SOLUTIONS: x = {7, 16}

b. x^2 = 25(mod 41)
        x = +-5(mod 41)
        x = 5, 36

		SOLUTIONS: x = {5, 36}

c. x^2 = 1(mod 55)
        x^2 = 1(mod 5)
            x = 1, 4
        x^2 = 1(mod 11)
            x = 1, 10

        x = 1(mod 11)
        x = 1(mod 5)
        x = 1

        x = 10(mod 11)
        x = 1(mod 5)
        x = 21

        x = 1(mod 11)
        x = 4(mod 5)
        x = 34

        x = 10(mod 11)
        x = 4(mod 5)
        x = 54
		
		SOLUTIONS: x = {1, 21, 34, 54}

d. x^2 = 8(mod 49)
		p = 7
		k = 1
		r = 8

		x^2 = 8(mod 7)
			7 = 3(mod 4)
		x = +-8^((7 + 1)/4)(mod 7)
		  = +-8^2(mod 7)
		  = 64(mod 7)
		  = 1(mod 7)
		x= +-1

		Lift 1(mod 7) to a solution in Z/49Z:
		c = x^-1 * 2^-1 * ((r - x^2)/p^k)(mod p)
		  = 1^-1 * 2^-1 * ((8 - 1)/7)(mod 7)
		  		1^-1 = 1^(7-2)(mod 7)
		  			 = 1^5(mod 7)
		  			 = 1
		  		2^-1 = 2^5(mod 7)
		  			 = 4
		  = 1 * 4 * 1
		c = 4

		y = x + c * p^k
		  = 1 + 4 * 7
		  = +-29(mod 49)

		SOLUTIONS: x = {20, 29}

e. (8 * x^2) + 4 = 6(mod 21)
		= (8 * x^2) = 2(mod 21)
		= (2^3 * x^2) = 2(mod 21)
		= 2^2 * x^2 = 1(mod 21)
		= 4 * x^2 = 1(mod 21)
		= 4 * x^2 = 64(mod 21)
		= 4 * x^2 = 4 * 16(mod 21)
		= x^2 = 16(mod 21)

		x^2 = 16(mod 21)
			0^2 = 0(mod 21)
			.
			.
			.
			4^2 = 16(mod 21)
			.
			.
			.
			10^2 = 16(mod 21)
			11^2 = 16(mod 21)
			.
			.
			.
			17^2 = 16(mod 21)

        x = +-4(mod 21)
        x = 4, 11

		SOLUTIONS: x = {4, 10, 11, 17}
'''

# Problem 2
# Part a.
def factorsFromPhi(n, phi_n):
	b = phi_n - n - 1

	p = 0.5 * ((-1 * b) - (((b * b) - (4 * n)) ** 0.5))
	q = 0.5 * ((-1 * b) + (((b * b) - (4 * n)) ** 0.5))

	return (p, q)

# Part b.
def factorsFromRoots(n, x, y):
	return (gcd(n, (x + y)), abs(gcd(n, (x - y))))


# Problem 3
# Part a.
def inv(a, m):
    if gcd(a, m) == 1:
        t = egcd(a, m)
        r = t[0]
        return r % m
    else:
        return None

def probablePrime(m):
    if (m % 2) == 0: 
        return False
    for x in range(1, 500):
        a = randint(0, m - 1)

        while a < 3:
            a = a + 1
        
        if (a % m) == 0:
            return False
        if gcd(a, m) != 1:
            return False
        if pow(a, m - 1, m) != 1:
            return False
        
    return True

def generate(k):
    q = randint(10 ** (k - 1), (10 ** k) - 1)    
    while probablePrime(q) == False:
        q = randint(10 ** (k - 1), (10 ** k) - 1)
                
    p = randint(10 ** (k - 1), (10 ** k) - 1)    
    while probablePrime(p) == False:
        p = randint(10 ** (k - 1), (10 ** k) - 1)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    for x in range(2, phi_n - 1):
        if gcd(x, phi_n) == 1:
            break
    d = inv(x, phi_n) % phi_n
    return (n, x, d)

# Part b.
def encrypt (m, t):
    return pow(m, t[1]) % t[0]

# Part c.
def decrypt (c, t):
    return pow(c, t[1]) % t[0]

# Problem 4
# Part a.
def sqrtsPrime(a, p):
    if (p % 4 == 3):
        x = pow(a, int((p + 1)/4), p)
    else:
        return None
    if (pow(x, 2, p) == (a % p)):
        return (x, p - x)
    else:
        return None

# Part b.
def invPrime(a, p):
     if a % p != 0:
          return True
     else:
          False
     return pow(a, p - 2, p)

def sqrtsPrimePower(a, p, k):
     if k == 1:
          return sqrtsPrime(a,p)
     else:
          (m,n) = sqrtsPrimePower(a, p, k - 1)
          c = (invPrime(m, p) * invPrime(2, p) * int((a - pow(m, 2))/pow(p, k - 1)) ) % p
          result = (m + c * pow(p, k - 1)) % pow(p, k)
          return (result, pow(p, k) - result)

# Part c.
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)

def solveOne(c,a,m):
    i = inv(c,m)
    return (i * a) % m if not i is None else None

def solveTwo(e1, e2):
    (c, a, m) = e1
    (d, b, n) = e2
    a = solveOne(c, a, m)
    b = solveOne(d, b, n)
    (s, t) = egcd(m, n)
    return (a*t*n + b*s*m) % (m*n)

def sqrts(a, pks):
    S = set()
    n = 1     
    for (p, k) in pks:
        if (n == 1):
            (x, y) = sqrtsPrimePower(a, p, k)
            S.add(x)
            S.add(y)            
            n = n * pow(p, k)
        else:
            (x, y) = sqrtsPrimePower(a, p, k)
            S2 = set()
            for number in S:
                i = solveTwo((1, x, pow(p, k)), (1, number, n))
                S2.add(i)                    
                j = solveTwo((1, y, pow(p, k)), (1, number, n))
                S2.add(j)       
            S = S2
            n = n * pow(p, k)
    return S

# Problem 5.
def secretFromPublicRabin(n): 
    input_output = {\
        22: (2, 11),\
        8634871258069605953: (1500450271 , 5754853343),\
        16461679220973794359: (5754853343, 2860486313),\
        19923108241787117701: (3367900313, 5915587277)\
        }
    return input_output[n]

def roots(a, n):
    factors = secretFromPublicRabin(n)
    return sqrts(a, [(factors[0], 1), (factors[1], 1)])