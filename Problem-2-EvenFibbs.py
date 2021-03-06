### PROBLEM 2 - EVEN FIBONACCI NUMBERS

# The Problem - Consider the terms in the Fibonacci sequence
# whose values do not exceed 4,000,000 - find the sum of the
# even valued terms.

# The Code

# Generation of the Fibonacci numbers
i = 0
limiter = 10000000 # will be 4 mill once we've checked everything

t1 = 0
t2 = 1

even_stevens = 0
odd_cods = 0

seq = []

# Generating the sequence
while i < limiter:
    new = t1 + t2

    t1 = t2
    t2 = new

    seq.append(new)

    if seq[i]%2 == 0:
        even_stevens += seq[i]
    else:
        odd_cods += seq[i]
    
    if seq[i] <= 4000000:
        i += 1
    elif seq[i] >= 4000000:
        break

print("Sum of Even Terms = " + str(even_stevens))
#print("Sum of Odd Terms = " + str(odd_cods))

# I'm being lazy I can't be bothered to move the even indices 
# etc. so the even terms are going to be the odd indicies in 
# python


