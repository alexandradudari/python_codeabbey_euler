def josephus_recursive(n: int, k: int) -> int:
    """Given number of people n and constant step k, return the position
       of a person who remains the last."""
    
    if n == 1:
        return 0
    else:
        return((josephus_recursive(n-1, k) + k) % n)
    
