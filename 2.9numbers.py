# 2.9 numbers: total cost
#Statement
#A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

# Read an integer:
# number cupcake input 2
a = int(input())
#amout of dollars input 10
b = int(input())
#amount of cents input 15
c = int(input())

#dollars 10
d = (a * b)
#cents 15
e = (a * c)

# Print a value:
print(d, e)