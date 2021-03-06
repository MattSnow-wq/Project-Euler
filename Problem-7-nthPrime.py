### PROBLEM 7 - 10001st PRIME

# The Problem: Find the 10,001st prime number

# The Code:
# Let's just use an import prime library - the thought process:
# People spend a long time writing these libraries, any solution
# they have is almost certainly better than mine
from primesieve import nth_prime as nprime

print("The 10,001st prime number is %d" %nprime(10001))
