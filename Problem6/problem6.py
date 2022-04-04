# This could be solved programatically with a couple for loops, but it is a
# rather simple computation. We know that 1^2 + ... n^2 is equal to the
# expression (n(n+1)(2n+1))/6. We also know that (1 + ... n)^2 is equal to the
# expression (n^2(n+1)^2)/4. I could work through the proofs on these here,
# but it wouldn't add anything to the solution.

n = 100
print((n ** 2 *(n+1)**2)/4 - (n*(n+1)*(2*n+1))/6)