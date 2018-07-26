def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor between two numbers."""
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def sm(a: int, b: int) -> int:
    """Return the smallest multiple between two numbers."""
    return (a * b) // gcd(a, b)


