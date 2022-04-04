# A palindrome made via the product of two 3 digit numbers will be of the form
# abccba where a, b, and c are digits betwen 0-9. Factoring this will give us
# the insight that the palindrome will satisfy this expression: 
# 11(9091a + 910b + 100c). Knowing the product is divisible by a prime means
# one of the 3 digit numbers must be divisible by 11. We can now solve the
# problem using the code below

i = 999
j = 990
largest_palindrome = num1 = num2 = 0
while (i > 100):
    j = 990
    while (j > 100):
        product = i * j
        if (product > largest_palindrome):
            if (str(product) == str(product)[::-1]):
                largest_palindrome = product
                num1 = i
                num2 = j
        j -= 11
    i -= 1
print(largest_palindrome)