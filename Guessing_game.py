from random import randint
import sys


# Takes in higher and lower bound and asks for an integer that's within range and returns it
def guess(num1, num2):
    while True:
        try:
            choice = int(input(f"What is your guess {num1} to {num2} "))
        except ValueError:
            print("Please enter an integer")
        else:
            if (choice >= num1) and (choice <= num2):
                return choice
            else:
                print(f"Please enter an integer within range {num1} and {num2}. ")


# Gets upper and lower bound and returns it.
def get_range():
    while True:
        try:
            low = int(input("What is your lowest Value? "))
        except ValueError:
            print("Your lower bound needs to be an integer.")
        else:
            while True:
                try:
                    high = int(input("What is your highest Value? "))
                except ValueError:
                    print("Your higher bound needs to be an integer.")
                else:
                    if low < high:
                        return low, high
                    else:
                        print("Your higher bound needs to be more than your lower bound.")


# Checks to see if any sys arguments have been input if they have returns them. With low and high bound.
def check_arg():
    try:
        num1 , num2 = int(sys.argv[1]), int(sys.argv[2])
    except (IndexError, ValueError):
      return False, False
    else:
        if num1 < num2:
            return num1, num2
        elif num1 == num2:
            return False, False
        else:
            return num2, num1

# Asks user if they want to replay the game returns True if they do and False if they don't
def replay():
    retry = input("Do you want to play again? y or n?: ")
    if retry[0].capitalize() == "Y":
        return True
    else:
        print("Thanks for playing")
        return False

#Main Game logic
def play_game():
    print("Welcome to the Guessing game")
    play = True
    replayer = False
    while play:

        # Initial Start up
        guessing = True
        num1, num2 = check_arg()
        if replayer or num1 == False:
            num1, num2 = get_range()

        answer: int = randint(num1, num2)

        # Start guessing
        while guessing:
            choice = guess(num1, num2)

            if answer == choice:
                print("Your answer is correct!")
                guessing = False
            elif abs(choice - answer) < 5:
                print("You are close!!!!")
            else:
                print("Whoops try again!")
        replayer = replay()
        play = replayer
        if play:
            continue
        else:
            break
