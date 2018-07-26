def josephus(n: int, k: int) -> int:
    """Given number of people n and constant step k, return the position
       of a person who remains the last."""
    
    result = 0
    for i in range(2, n+1):
        result = (k + result) % i
    return (result + 1)

n, k = input().split()
print(josephus(int(n), int(k)))
