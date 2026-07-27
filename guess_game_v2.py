import random

secret = random.randint(1, 100)
count_of_try = 0

def check_guess(guess, secret):
    if guess < secret:
        return "too low"
    elif guess == secret:
        return "correct"
    else:
        return "too high"

while True:
    guess = int(input("your guess: "))
    result = check_guess(guess, secret)
    if result == "too low":
        print("too low")
        count_of_try += 1
    elif result == "correct":
        print("correct")
        count_of_try += 1
        print(f"You had tried for {count_of_try} time/s")
        break
    else:
        print("Too high")
        count_of_try += 1

    print(f"You had tried for {count_of_try} time/s")
    
#while True:
#    guess = int(input("your guess: "))
#    if guess < secret_number:
#        print("too low")
#        count_of_try +=1
#    elif guess == secret_number:
#        count_of_try +=1
#        print(f"Congratulation, you are right. You had tried for {count_of_try} time/s")
#        break
#    else:
#        print("Too high")
#        count_of_try +=1
#    print(f"You had tried for {count_of_try} time/s")