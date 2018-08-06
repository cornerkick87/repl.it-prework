# 2.4 numbers: tens digit
#Statement
#Given an integer, print its tens digit.

# Read an integer:
a = int(input())

b = ( a // 10)
c = ( a % 10)
d = ( b % 10)

# Print a value:
print(f'{d}')