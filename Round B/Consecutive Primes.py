# Google Kick Start 2021 Round B - Consecutive Primes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6

# input: a number
# output: largest number less than or equal to Z 
# that is the product of two consecutive prime numbers

import math

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i * i > n:
            return True
        if n % i == 0:
            return False
    return True

def find_prime(n):
    m = math.sqrt(n)
    x = int(m)
    while x * x < n:
        x += 1
    # largest prime smaller than or equal to √n
    small = 0
    for i in range(x-1, 1, -1):
        if check_prime(i):
            small = i
            break
    
    # smallest prime greater than √n 
    big = 0
    for i in range(x, n):
        if check_prime(i):
            big = i
            break
    
    if small * big  <= n:
        return small * big
   
    for i in range(small-1, 1, -1):
        if check_prime(i):
            return i * small
    return None
    
for i in range(int(input())):
   print("Case #"+str(i+1), end=": ")
   print(find_prime(int(input())))
