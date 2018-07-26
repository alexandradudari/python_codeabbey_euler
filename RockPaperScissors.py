def RPS(matches: list) -> int:
    """Given several records of the played games of 'Rock Paper Scissors',
       specify whether first player wins (by value 1) or second (by value 2)."""
    
    draws = ['PP', 'SS', 'RR']
    player_one = ['RS', 'PR', 'SP']

    count_one = 0
    count_two = 0
    
    for match in matches:
        if match in draws:
            continue
        elif match in player_one:
            count_one += 1
        else:
            count_two += 1
            
    if count_one > count_two:
        return 1
    else:
        return 2

n = input()
for i in range(int(n)):
    matches = input().split()
    print(RPS(matches), end=" ")
    
