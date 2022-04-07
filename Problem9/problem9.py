from math import sqrt

# Question can be found at https://projecteuler.net/problem=9

for a in range(1001):
    for b in range(a, 1001):
        c = sqrt(a ** 2 + b ** 2)
        if c % 1 == 0 and a + b + c == 1000 and (a != b and c > a and c > b):
            print(a * b * c)
            break

