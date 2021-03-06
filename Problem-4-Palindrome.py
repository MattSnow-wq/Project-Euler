### PROBLEM 4 - LARGEST PALINDROME PRODUCT

# The Problem: Find the largest palindrome made from the 
# product of two 3-digit numbers (for example, the largest
# palindrome made from 2-digits is 9009 = 91 x 99)

# The Code:

# Some known values
# --------------------------------------------------------------------------{{{
pal1 = 90109 # five long (odd)
pal2 = 28377382 # eight long (even)
npal1 = 12345 # five long (odd)
npal2 = 92865829 # eight long (even)
# --------------------------------------------------------------------------}}}

# Function to detect Palindrome (isPal(x))
# --------------------------------------------------------------------------{{{

def isPal(x):
    """ This will take an integer in, convert to a string and
    test if it's a palindrome or not - it will return TRUE if it
    is a Palindrome, and FALSE if it isn't
    """
    case = str(x)
    case.split()
    
    odds = False
    even = False
    
    if len(case)%2 == 0:
        odds = True
    else:
        even = True

    err = 0
    
    # Splitting cases into odd or even trials
    if odds == True:
        for i in range(0,len(case)):
            if case[i] != case[-(i+1)]:
                err += 1
   
    elif even == True:
        for i in range(0,len(case)-1):
            if case[i] != case[-(i+1)]:
                err += 1
    
        if case[len(case)-2] != case[len(case)-1]:
             err +1

    if err != 0:
        return False
    elif err == 0:
        return True

# --------------------------------------------------------------------------}}}

# Creating set of possibles
# --------------------------------------------------------------------------{{{
allposs = []

for i in range(100,999):
    for j in range(100,999):
        allposs.append(i*j)
# --------------------------------------------------------------------------}}}

# Removing the palindromes into a new list
# --------------------------------------------------------------------------{{{
palposs = []

for i in range(0,(len(allposs)-1)):
    if isPal(allposs[i]) == True:
        palposs.append(allposs[i])
# --------------------------------------------------------------------------}}}

# Finding the maximum
# --------------------------------------------------------------------------{{{
palposs.sort()

answer = palposs[len(palposs)-1]
print("The answer is: " + str(answer))

# --------------------------------------------------------------------------}}}

