import random
from typing import Any, Union

print("Hello, this is the game - 'Guess the number from 1 to 100.'")
print("Your tries count set to 6.")
print("Enter q to quit.")
number = random.randint(1,101)
tries = 6

while tries >= 0:
    if tries == 0:
        lost_message = input("\nYou ran out of attempts. Wanna try again? (yes/no): ")
        if lost_message == "yes":
            tries = 6
            continue
        else:
            break
    message = input("\nPlease enter your number: ")
    if message == "q":
        break
    try:
        message = int(message)
    except:
        print("Your input is incorrect value. Please use numbers only.")
        continue

    if message < 0 or message > 100:
        print("Your number is out of range.")
        tries -= 1
        continue
    if message < number:
        print("This number is lower than expected.")
    elif message > number:
        print("This number is higher than expected.")
    elif message == number:
        print("You guessed it right!")
        ask_again = input("\nDo you wanna play another game? (yes/no): ")
        if ask_again == "yes":
            tries = 6
            continue
        else:
            break

    tries -= 1
    print("Tries left: " + str(tries))

print("\nGame over.")


