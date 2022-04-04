# Question can be found at https://projecteuler.net/problem=7
#
# Functions from prime_kit.py are in the Helpers/prime_kit/__init__.py file in
# the repo.

from prime_kit import sieve_of_eratosthenes as sieve

primes = sieve(105000)
print(primes[10000])