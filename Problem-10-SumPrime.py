### PROBLEM 10 - SUMMATION OF PRIMES

# The Problem: Find the sum of all the primes below two million

# The Code:
# Learning from Problem 7 - to the prime sieve!
from primesieve import primes as sieve

x = sieve(2000000)
ans = 0
for n in x:
    ans += n

print("The summation: ", ans)

