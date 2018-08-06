# 2.3 numbers:last two digits
#Statement
#Given an integer greater than 9, print its last two digits.

# Read an integer:
a = int(input())
#tens place
b = (a // 10)
#ones place
c = ( a % 10)
d = ( b % 10)
# Print a value:
print(f'{d}{c}')