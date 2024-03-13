import random

answer = random.randint(1,10)
chances = 0

while chances < 5:
    guess = int(input("Enter the number between 1 to 10: "))

    if guess > answer:
        print("You have entered the number which is too high")
    elif guess < answer:
        print("You have entered the number which is too low")
    else:
        print("Congratulations you won the game!")

    chances += 1
    if chances ==5:
        print("Game Over.")