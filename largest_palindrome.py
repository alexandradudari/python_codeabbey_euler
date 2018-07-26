def is_palindrome(n):
    n = str(n)
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] != n[j]:
            return False
        i += 1
        j -= 1
    return True

def largest_palindrome():
    result = 0
    for i in range(990, 99, -11):
        for j in range(999, 99, -1):
            temporar = i * j

            if result < temporar and is_palindrome(temporar):
                result = temporar
                break
            elif temporar < result:
                break
    return result

print(largest_palindrome())
