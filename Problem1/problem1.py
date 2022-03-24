# The sum of all multiples of some integer a less than some constant 
# n can be found by finding the largest multiple under n, dividing by a,
# and summing continuously from 1 to that result. Then multiply by a again and
# you have your final sum.

threes = (333 * (333 + 1)/2) * 3
fives = (199 * (199 + 1)/2) * 5

# numbers which are multiples of both 3 and 5 are counted twice with the above
# method, so we need to subtract that set once.

doubles = (66 * (66 + 1)/2) * 15
print(threes + fives - doubles)