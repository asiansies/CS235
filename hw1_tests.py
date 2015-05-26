# Tester: T, T, F
print('Problem 1a:')
print(isSymmetric({1,2}, {(1,1), (2,2), (2,1), (1,2)}))
print(isSymmetric({1,2,3}, {(1,2), (2,1), (3,3)}))
print(isSymmetric({'a','b','c'}, {('a','a'), ('b','b'), ('a','c')}))

# Tester: T, F, T, F
print('\nProblem 1b:')
print(isEquivalence({1,2,3}, {(1,1), (2,2), (3,3)}))
print(isEquivalence({1,2,3}, {(1,2), (2,1), (3,3)}))
print(isEquivalence({1,2}, {(1,1), (2,2), (1,2), (2,1)}))
print(isEquivalence({0,3,6}, {(0,3), (3,6), (0,6), (3,0), (6,3), (6,0)}))

# Tester: T, T
print('\nProblem 2a:')
print(isEquivalence(X1,R1))
print(quotient(X1,R1) == {frozenset({"a", "b"}), frozenset({"c", "d"})})

# Tester: T, T
print('\nProblem 2b:')
print(isEquivalence(X2,R2))
print(quotient(X2,R2) == {frozenset({0,3}), frozenset({1,4}), frozenset({2,5})})

# Tester: T, T
print('\nProblem 2c:')
#print(isEquivalence(X3,R3))
print(quotient(X3,R3) == {frozenset(range(-1000,0)), frozenset({0}), frozenset(range(1,1001))})

# Tester: {3}, {2,7}
print('\nProblem 3a:')
print(properPrimeFactors(9))
print(properPrimeFactors(14))

# Tester 
print('\nProblem 3b:')
print(disjoint({2,3,4,5,6}))
print(disjoint({2,4,8}))

print('\nProblem 3c:')
print(isSymmetric(symmetric, disjoint(symmetric)))
print(isSymmetric(symmetric, disjoint(reflexive)))
print(isSymmetric(symmetric, disjoint(transitive)))

# Tester
print('\nProblem 4a:')
print(square(9))
print(square(12))

# Tester: {(3,4), (4,3)},  {(3,4), (4,3), (3,5), (5,3), (4,5), (5,4), (5,12), (12,5)}
print('\nProblem 4b:')
#print(pythagorean({3,4}))
#print(pythagorean({3,4,5,12}))
print(len(S))
print(len(pythagorean(S)))

# Tester
print('\nProblem 4c:')
print(anotherPrimeSquare([81,49]))
print(anotherPrimeSquare([1,9]))