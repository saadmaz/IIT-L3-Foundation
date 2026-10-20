import random
import time

def random_cavee():
    cavee = ["Gobbless you down!", "Greets you and then gives you his treasure!"]
    return random.choice(cavee)

while True:
    print("You are in the kingdom of dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is friendly and will share his treasure with you.\nThe other dragon is hungry and will eat you on sight.")
    
    cave = ['', 'Cave 1', 'Cave 2', 'Cave 3', 'Cave 4', 'Cave 5']

    try:
        number = int(input("Cave 1, 2, 3, 4, or 5? "))
        print("You're in cave:", cave[number])
    except IndexError:
        print("No such cave found")
        continue
    else:
        print("Cave found")

    time.sleep(2)
    print("You approach the cave...\nA large dragon jumps in front of you!\nHe opens his jaws and...")
    time.sleep(1)
    print(random_cavee())

    # Prompt the user to continue or end the game
    user_input = input("Do you want to continue? (yes/no): ")
    
    if user_input.lower() == "yes":
        continue  # Restart the loop and begin the game again
    elif user_input.lower() == "no":
        print("Thank you for playing. Goodbye!")
        break  # End the loop and exit the game
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Game ended.")