from math import sqrt

# Question can be found at https://projecteuler.net/problem=12

num = 1
diff = 2
while True:
    num = num + diff
    diff += 1
    div = 1
    div_count = 0
    while div <= sqrt(num):
        if num % div == 0:
            if int(num/div) == div:
                div_count += 1
            else:
                div_count += 2
        div += 1
    if div_count >= 500:
        break
print(num)