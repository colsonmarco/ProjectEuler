from sympy import sieve
from sympy.ntheory import sieve

# Question can be found at https://projecteuler.net/problem=10

sieve.extend(2000000)
print(sum(sieve._list))