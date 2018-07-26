def checksum(numbers: list) -> int:
    """For a list of integer numbers, checksum is some derived value
       calculated using all the members of a list in some whimsical way.
       Return a single value - calculated checksum."""
    result = 0
    for num in numbers:
        result = ((result + num) * 113) % 10000007
    return result


def bubble_array(numbers: list) -> int,int:
    """Return the number of performed swaps after one iteration in a list.
       Return the value for the checksum, after processing."""
    swaps = 0
    length = len(numbers) - 1

    for i in range(0, length):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            swaps += 1
    check = checksum(numbers)
    print(swaps, check)



numbers = [int(x) for x in input().split()]
numbers = bubble_array(numbers[:-1])


