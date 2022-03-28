from prime_kit import prime_factors

# We can solve this problem computationally using fermat's little theorem to
# check for primality and then prime factorization. More efficient methods
# could be used, but for such small numbers, it's unnecessary.
# 
# Functions from prime_kit.py are in the Helpers/prime_kit/__init__.py file in
# the repo.

print(max(prime_factors(600851475143)))