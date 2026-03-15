"""
TODO-based exploration of number theory with SymPy.
Author: Miguel Vargas Martin using SymPy manual and ChatGPT
Last modified: January 2026

Instructions:
- Read each TODO carefully.
- Before running a line, try to predict its output.
- Uncomment lines only when instructed.
- Answer the questions in the comments or in a separate worksheet.
"""

import warnings
warnings.filterwarnings('ignore')

from sympy import *

# TODO 1: Basic integers

a, b, n = 3, 18, 25

# TODO 1.1:
# Predict gcd(a, b). Then uncomment and verify.
# print(igcd(a, b))

# TODO 1.2:
# Predict lcm(a, b). What is the relationship between gcd and lcm?
# print(ilcm(a, b))

# TODO 1.3:
# List all positive divisors of n.
# How does this relate to the prime factorization of n?
# print(divisors(n))

# TODO 1.4:
# How many divisors does n have?
# print(divisor_count(n))

# TODO 1.5:
# Find the prime factorization of n.
# print(factorint(n))


# TODO 2: Primality

# TODO 2.1:
# Is n prime? Why or why not?
# print(isprime(n))

# TODO 2.2:
# Pick a different value for n that *is* prime and test it.


# TODO 3: Euler's Totient Function

from sympy.ntheory import totient

# TODO 3.1:
# Compute φ(a), φ(b), and φ(n).
# What does φ(n) count?
# print(totient(a))
# print(totient(b))
# print(totient(n))

# TODO 3.2:
# Verify φ(p) = p − 1 for a prime p of your choice.


# TODO 4: Chinese Remainder Theorem (CRT)

from sympy.ntheory.modular import crt

# Solve the system:
#   x ≡ 49 (mod 99)
#   x ≡ 76 (mod 97)
#   x ≡ 65 (mod 95)

# TODO 4.1:
# Before running this, check whether the moduli are pairwise coprime.
solution = crt([99, 97, 95], [49, 76, 65])
print(solution)

# TODO 4.2:
# Extract the solution x and verify each congruence manually.


# TODO 5: Miller–Rabin Primality Test

from sympy.ntheory.primetest import mr

# TODO 5.1:
# The number below is large. Do you expect it to be prime?
print(mr(1373651, [2, 3, 5]))

# TODO 5.2:
# Change the bases. Does the result change?
# Why is Miller–Rabin called a "probabilistic" test?


# TODO 6: Primitive Roots

# TODO 6.1:
# Is a a primitive root modulo n?
print(is_primitive_root(a, n))

# TODO 6.2:
# Find a primitive root modulo n (if one exists).
g = primitive_root(n)
print(g)

# TODO 6.3:
# Verify that g generates all units modulo n.


# TODO 7: Discrete Logarithm

from sympy.ntheory import discrete_log

# Solve: find x such that 7^x ≡ 15 (mod 41)
x = discrete_log(41, 15, 7)
print(x)

# TODO 7.1:
# Verify the result by computing 7**x % 41.
# TODO 7.2:
# Why is the discrete logarithm problem considered hard in general?
