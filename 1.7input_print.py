# 1.7 input /print: two timestamps
#Statement
#Given a two-digit integer, print its left digit (a tens digit) and then its right digit (a ones digit). Use the operator of integer division for obtaining the tens digit and the operator of taking remainder for obtaining the ones digit. 

#ANSWER
# Read an integer:
a = int(input())
#tens place
b = ( a // 10)
#ones place
c = ( a % 10)

# Print a value:
print(b, c)