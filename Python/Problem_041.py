#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 41
What is the largest n-digit pandigital prime that exists?
'''
import math
from itertools import permutations
# is_prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

pp_list = []
# Since the pandigital numbers made by n=5, 6, 8, 9 are all divisible by 3, 
# we need to serch only for the case of n=7.
pl = permutations(range(1, 8))
for p in pl:
    a = int(''.join(map(str, p)))
    if is_prime(a):
        pp_list.append(a)

print(max(pp_list))