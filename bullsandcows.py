def mastermind(secret: str, guess: str) -> int:
    """Take a secret number and a guess. Return a hint consists of two values:
       -first tells how many digits are guessed correctly and are in correct positions;
       -second tells how many digits are guessed correctly but are in wrong positions."""
    correct_place = 0
    wrong_place = 0
    for i in range(4):
        if secret[i] == guess[i]:
            correct_place +=1
        elif guess[i] in secret:
            wrong_place += 1
    print("{}-{}".format(correct_place, wrong_place), end=" ")


secret, num_guesses = input().split()
guesses = input().split()
for guess in guesses:
    mastermind(secret,guess)
