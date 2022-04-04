import os

# Question can be found at https://projecteuler.net/problem=8
#
# This problem does not have a significantly more efficient solution than
# iterating through the digits and comparing the products. That's what we'll
# do here.

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__, "digits.txt"))
digits = file.read().replace('\n', '')
file.close()

max_product = 0

for i in range (0, len(digits)-12):
    adjacent_product = 1
    adjacent_chars = digits[i:i+13]
    for char in adjacent_chars:
        adjacent_product *= int(char)
    max_product = max(max_product, adjacent_product)

print(max_product)