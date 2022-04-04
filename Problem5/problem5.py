# This problem does not require any programming, we can find the prime
# factorization of every number between 1-20 inclusive, then multiply the
# largest power of each prime together:
# 20 = 2^2 * 5
# ...
# 2 = 2^1
# Taking the largest prime factors from the computation we get the following:
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

print(2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19)