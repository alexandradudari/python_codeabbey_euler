def lcg(a: int, c: int, modulus: int, seed: int, member: int) -> int:
    """Return the n-th member's value calculated with discontinuous
       piecewise linear equation."""
    for i in range(member):
        seed = (a * seed + c) % modulus
    return seed


n = int(input())
for i in range(n):
    a, c, modulus, seed, member = [int(x) for x in input().split()]
    result = lcg(a, c, modulus, seed, member)
    print(result, end=" ")
