cache = {}


def factorial(n: int) -> int:
    """Return n factorial."""
    if n in cache:
        return cache[n]

    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
    cache[n] = result
    return result


def combinations_counting(n: int, k: int) -> int:
    """Return how many combinations of k elements from the set n exist."""
    result = factorial(n) // (factorial(k) * factorial(n-k))
    return result


n = int(input())
for i in range(n):
    n, k = input().split()
    print(combinations_counting(int(n), int(k)), end=" ")
