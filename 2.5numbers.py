# 2.5 numbers: sum of digits
#Statement
#Given a three-digit number. Find the sum of its digits.

#answer
# Read an integer:
a = int(input())
b = (a % 10)
c = (b % 10)

# Print a value:
print(b + c)