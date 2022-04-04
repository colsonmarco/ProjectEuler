# Question can be found at https://projecteuler.net/problem=2
#
# You can solve this problem without code. The golden ratio (phi) is
# the ratio between consecutive terms. Since the even terms are every third
# term, the ratio between even terms approaches phi^3 (4.236068). Thus, we
# can start with the first even term, and multiply by phi^3 then sum each of
# these values.

res = 0
term = 2
while term < 4000000:
    res += term
    term = round(term * 4.236068)
print(res)

# Solving this problem through code is also quite simple since each even term
# is every third term, thus a simple while loop will suffice.

res = 0
term1 = 1
term2 = 1
count = 2
while term2 < 4000000:
    if count == 3:
        count = 0
        res += term2
    tempvar = term2
    term2 = term1 + term2
    term1 = tempvar
    count += 1
print(res)

# Both solutions print the same answer.