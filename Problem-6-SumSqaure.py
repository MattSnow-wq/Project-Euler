### PROBLEM 6 - SUM SQUARE DIFFERENCE

# The Problem:
# For the 1st 100 natural numbers - find the difference between
# the sum of the squares of each (1^2 + 2^2 + ...) and the
# the square of the sum ([1 + 2 + ...]^2)

# The Code:
sum_of_squares = 0
square_of_sum = 0

vari = 0

for j in range(0,101):
    vari += j

# Sum of the Squares:
for i in range(0,101):
    sum_of_squares += i**2

# Square of the Sum:
square_of_sum = vari**2

# Difference
print("Sum of the Squares: " + str(sum_of_squares))
print("Squares of the Sum: " + str(square_of_sum))

diff = -sum_of_squares + square_of_sum
print("The Difference: " + str(diff))

