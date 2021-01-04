### PROBLEM 1 - MULTIPLES OF 3 AND 5

# The Problem:
# For the natural numbers less than 1000, what is the 
# sum of ALL the multiples of 3 or 5?

# The Code:

# Brute force - check if multiple of 3 then 5
# and if they are then add them to a counter

counter = 0

for i in range(0,1000):
    
    if i%3 == 0 or i%5 == 0:
        counter += i
    elif i%3 ==0 and i%5 == 0:
        counter += i

print("The sum of multiples on 3 and 5 below 10 is "+str(counter))
