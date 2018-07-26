from math import ceil
from math import sqrt

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor between a and b."""
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def triplets(target: int) -> int:
    """Return the product of a Pythagorean triplet, for which,
       the sum of a, b and c is equal with target."""
    new_target = target // 2
    mlimit = ceil(sqrt(new_target)) - 1
    for m in range(2, mlimit+1):
        if new_target % m == 0:
            sm = new_target // m
            while sm % 2 == 0:
                sm = sm // 2

            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1

            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = new_target // (k * m)
                    n = k - m
                    a = d * (m ** 2 - n ** 2)
                    b = d * (2 * m * n)
                    c = d * (m ** 2 + n ** 2)
                    return a * b * c
                    
                k = k + 2

n = int(input())
for i in range(n):
    a = int(input())
    print(triplets(a), end=' ')
