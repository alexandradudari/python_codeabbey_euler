cache = {}


def fibonacci(n: int) -> int:
    """Generate Fibonacci sequence."""
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


def check_divisibility(n: int) -> int:
    """Print the index of the first non-zero member of the Fibonacci sequence
       which is evenly divisible by n."""
    for number in fibonacci_numbers:
        if number == 0: continue
        if number % n == 0:
            print(fibonacci_numbers.index(number), end=" ")
            break


fibonacci_numbers = []

for i in range(0, 10000):
    fibonacci_numbers.append(fibonacci(i))

count = input().split()
numbers = input().split()

for number in numbers:
    check_divisibility(int(number))

