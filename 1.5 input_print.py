# 1.5 input/print Apple sharing
#Statement
#N students take K apples and distribute them among each other evenly. The remaining (the indivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

#The program reads the numbers N and K. It should print the two answers for the questions above.

# Read the numbers like this:
#students
n = int(input())
#apples
k = int(input())
#apples per student
a = (k // n)
#apples left in the basket
b = (k % n)
# Print the result with print()
print(a)
print(b)
# Example of division, integer division and remainder:
#print(63 / 5)
#print(63 // 5)
#print(63 % 5)