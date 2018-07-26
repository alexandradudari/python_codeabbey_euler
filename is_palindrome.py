def is_palindrome(phrase: str) -> bool:
    """Check if a phrase represents a palindrome."""
    
    phrase = ''.join([i for i in phrase if i.isalpha()]).lower()

    i = 0
    j = len(phrase) - 1

    while i < j:
        if phrase[i] != phrase[j]:
            return False
        i += 1
        j -= 1
    return True


n = int(input())
for i in range(n):
    phrase = input()
    
    if is_palindrome(phrase):
        print('Y', end=" ")
    else:
        print('N', end=" ")
