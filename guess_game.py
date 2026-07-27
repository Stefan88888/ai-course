import random
secret = random.randint(1, 100)
max_attempts = 8
attempts = 0

print("I'm thinking of a number between 1 and 100. You have 8 guesses")

while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts.")
        break
    elif guess < secret:
        print("No, too low.")

    else:
        print("No, too high.")

    print(f"Attempts left: {max_attempts - attempts}")
if attempts == max_attempts and guess != secret:
    print(f"Game over. The number was {secret}")