def bicycle_race(distance: int, speed_a: int, speed_b: int) -> float:
    """Return the distance between first city and rendezvous point
       (i.e. distance travelled by first cyclist before he meets the
       other cyclist)."""

    time = distance / (speed_a + speed_b)
    distance_travelled = speed_a * time
    return distance_travelled

n = int(input())
for i in range(n):
    distance, speed_a, speed_b = input().split()
    result = bicycle_race(int(distance), int(speed_a),int(speed_b))
    print(result, end=" ")
