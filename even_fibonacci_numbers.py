cache = {}

def fibonacci(n: int) -> int:
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

n = 0
x = 0
result = fibonacci(x)
while result <= 4000000:
    if result % 2 == 0:
        n += result
    x += 1
    result = fibonacci(x)
print(n)

