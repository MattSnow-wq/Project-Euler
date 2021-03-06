### PROBLEM 9 - SPECIAL PYTHAGOREAN TRIPLET

# The Problem: Find the SINGULAR Pythagorean triple (a^2+b^2=c^2)
# where a+b+c=1000 - find the product abc

# The Code:
from math import *

# Let's be (somewhat) smart about this - clever mathematicians
# have shown that Pythagorean triples (a,b,c) are related through
# the following:
# a = m^2-n^2
# b = 2mn
# c = m^2+n^2

# Right, so now we only need interate over values of m and n -
# the max of a,b,c has to be <1000 due to the problem, and so
# for the smallest limit (b=2mn), we know m or n can't be >500

a = 0
b = 0
c = 0

fina = 0
finb = 0
finc = 0

for n in range(1,500):
    for m in range(1,500):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        
        if a <= 0:
            pass
        elif a+b+c == 1000:
            fina = a
            finb = b
            finc = c
            prod = fina*finb*finc

# Printing (and confirming)
print("The Triplet: " )
print(fina)
print(finb)
print(finc)
print()

print("Values a^2, b^2 and c^2: ")
print(fina**2)
print(finb**2)
print(finc**2)
print()

print("Confirming it is Pythagorean triplet (should be 0): ")
print(fina**2-(fina**2-finb**2))

print("So the product abc: ")
print(prod)
print("and to double check...")
print(fina*finb*finc)
