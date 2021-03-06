### PROBLEM 3 - LARGEST PRIME FACTOR

# The Problem - What is the largest prime factor of the number
# 600851475134?

# The Code:
# We'll borrow some code from stackoverflow that runs in 
# 0(n) time - we'll comment ourselves the mathematics

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0: # if d is a factor we append it
            factors.append(d)
            n /= d # we reduce n by d and re-do
        d = d + 1

    return factors


pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs) 

print(pfs)
print(largest_prime_factor)


