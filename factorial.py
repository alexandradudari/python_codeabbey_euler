cache = {}

def factorial(n):
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
    cache[n] = result
    return result

print(factorial(3))
