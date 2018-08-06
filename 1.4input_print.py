# 1.4 input/ print: Previous and next
#Statement
#Write a program that reads an integer number and prints its previous and next numbers. See the example below.


# Read an integer:
a = int(input())
# Print a value:
print(a)
b = a + 1

c = a - 1
# turn a int back into a str use them before like below
# print(b)
print('The next number for the number ' + str(a) + ' is ' + str(b))
print('The previous number for the number ' + str(a) + ' is ' + str(c))


# or using python three use and f string which looks like this below!!!

# print(f'The next number for the number {a} is {b} ')
# print(f'The previous number for the number {a} is {c}')