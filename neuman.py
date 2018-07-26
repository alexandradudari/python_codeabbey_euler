def neumann_random_generator(n: int) -> int:
    """Report the number of iteration needed to come to repetition."""
    
    num_iteration = 0
    repeat_values = [str(n)]
    new_number = n ** 2
    no_iteration = True

    while no_iteration:
        if num_iteration != 0:
            new_number = int(new_number) ** 2
            
        new_number = str(new_number)
        
        if len(new_number) < 8:
            new_number = new_number.zfill(8)
        new_number = new_number[2:6]
        num_iteration += 1

        if new_number in repeat_values:
            no_iteration = False
            
        repeat_values.append(new_number)
    print(num_iteration, end=" ")


amount = input().split()
initial_values = input().split()

for value in initial_values:
    n = int(value)
    neumann_random_generator(n)
