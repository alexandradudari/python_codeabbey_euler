def largest_prime(n: int) -> int:
    """Return the largest prime factor of the number n."""
    b = 2
    while n > b:
        if n % b == 0:
            n = n // b
            b = 2
        else:
            b += 1
    return b
