from math import floor, sqrt, ceil
from bisect import bisect_left
from random import randint

def sieve_of_eratosthenes(num, start = 2):
    """
    Returns all prime numbers less than $num

    Args:
        num: An int specifying the upper bound under which to check for primes
    
    Returns: A list of ints representing all prime numbers less than $num
    """
    if start < 2:
        print("Start value must be greater than or equal to first prime (2).")
    prime_list = [i for i in range(start, num)]
    for i in prime_list:
        for j in range(2, floor(num / i) + 1):
            try:
                prime_list.remove(i * j)
            except:
                continue
    return prime_list


def prime_factors(num):
    """
    Returns all prime factors of a number

    Args:
        num: An int that the function will find the prime factors of

    Returns: All prime factors of $num
    """
    prime = 2
    factors = []
    while not probal_prime(num, 10):
        resultant = num/prime
        if num % prime == 0:
            num = int(resultant)
            factors.append(prime)
        else:
            prime = next_prime(prime)
    factors.append(num)
    factors = list(set(factors))
    factors.sort()
    return factors


def probal_prime(num, iterations):
    """
    Checks whether a $num is prime or not probabilistically using fermat's
    little theorem. The more $iterations, the more confidence in the resultant
    primality test.

    Args:
        num: The int which the function checks for primality
        iterations: An int specifying the amount of different trials to test
        for primaliy with, as it's a probabilistic method
    
    Returns: a bool that is true if $num is prime and false if it's not
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    for _ in range(iterations):
        a = randint(2, num - 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True


def next_prime(num):
    """
    Returns the next prime after the specified $num

    Args:
        num: An int representing the number to start the search for the next
        prime from.
    
    Returns: An int representing the next prime found after $num.
    """
    orig = num

    if num <= 2: return 3
    if num == 3: return 5
    if num <= 5: return 7

    num -= num % 6
    
    while True:
        if probal_prime(num + 5, 10) and num + 5 > orig: return num + 5
        if probal_prime(num + 6, 10) and num + 6 > orig: return num + 6
        if probal_prime(num + 7, 10) and num + 7 > orig: return num + 7
        num += 6


def take_closest(myList, myNumber):
    """
    Returns the closest value in a list to a target value

    Args:
        myList: A list containing the ints to match to the target value
        myNumber: the target value to search for the closest in the list
    
    Returns: The closest value in the list to the target value
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before