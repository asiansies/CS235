# Aihoa Le
# CS235: Algebraic Algorithms
# Assignment #1: Logic, Integers, Sets, and Relations

def quotient(X, R):
	return {frozenset({y for y in X if (x,y) in R}) for x in X}

def forall(X,P):
	S = {x for x in X if P(x)}
	return len(S) == len(X)

def exists(X, P):
	S = {x for x in X if P(x)}
	return len(S) > 0

def subset(X,Y):
	return forall(X, lambda x: x in Y)

# Problem 1a.
def isSymmetric(X, R):
	S = {(x,y) for x in X for y in X}
	T = {(y,x) for x,y in R}
	return subset(R, S) and subset(R, T)

# Problem 1b.
def implies(X, R):
	return X <= R

def isTransitive(X, R):
	S = {(x,y) for x in X for y in X}
	return subset(R,S) and forall(X, lambda x: forall(X, lambda y: forall(X, lambda z: implies((x,y) in R and (y,z) in R, (x,z) in R))))

def isReflexive(X, R):
	S = {(x,y) for x in X for y in X}
	return subset(R,S) and forall(X, lambda x: (x,x) in R)

def isEquivalence(X, R):
	S = {(x,y) for x in X for y in X}
	return subset(R,S) and isReflexive(X,R) and isSymmetric(X,R) and isTransitive(X,R)

# Problem 2a.
X1 = {"a", "b", "c", "d"}
R1 = {("a","a"), ("b","b"), ("c","c"), ("d","d"), ("a","b"), ("b","a"), ("c","d"),("d","c")}

# Problem 2b.
X2 = {0,1,2,3,4,5}
R2 = {(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (0,3), (3,0), (1,4), (4,1), (2,5), (5,2)}

# Problem 2c.
X3 = set(range(-1000, 1001))
R3 = {(x,y) for x in X3 for y in X3 if (x < 0 and y < 0) or (x > 0 and y > 0) or (x == 0 and y == 0)}

# Problem 3a.
def prime(p):
	return p > 1 and forall(set(range(2, p)), lambda n: p % n != 0)

def properPrimeFactors(n):
	return {x for x in set(range(1,n)) if n % x == 0 and prime(x)}

# Problem 3b.
def disjoint(S):
	P = {(x,x) for x in S if prime(x)}
	for x in S:
		X = properPrimeFactors(x)
		for y in S:
			Y = properPrimeFactors(y)
			I = {x for x in Y if x in X}
			if len(I) == 0:
				P.add((x,y))
	return P

# Problem 3c.
reflexive = {1,2}
symmetric = set()
transitive = {1,2,3}

# Problem 4a.
def square(n):
	return exists(set(range(0, n)),lambda k: k * k == n)

# Problem 4b.
def pythagorean(S):
	return {(a,b) for a in S for b in S if square((a*a) + (b*b)) or square((a*a) - (b*b)) or square((b*b) - (a*a))}

S = {1, 5, 7, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613}

# Problem 4c.
def anotherPrimeSquare(ps):
	S = set(range(0, max(ps)))
	aps = 0
	for x in S:
		if prime(x) and x not in ps:
			aps = x * x
	return aps