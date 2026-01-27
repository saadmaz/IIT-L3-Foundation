import random

#list of valid choices
choices = ('pinky', 'inky', 'polly')

#Initialize
player_score = 0
computer_score = 0
player_name = input("Enter Player name : ")

# Start a while loop that runs until the player decides to end the game.
while True:
    player_choice = input("Choose pinky, inky, or polly (or 'E' to End the game!): ")
    
    # If the player enters 'E', End the game
    if player_choice == 'E':
        break
    
    # If the player's choice is not a valid choice, print an error message and continue the loop
    if player_choice not in choices:
        print("Invalid choice, Try again.")
        continue
    
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    
    # Rules of the game
    if player_choice == computer_choice:
        outcome = "It's a tie!"
    elif player_choice == 'pinky' and computer_choice == 'inky' or \
         player_choice == 'inky' and computer_choice == 'polly' or \
         player_choice == 'polly' and computer_choice == 'pinky':
        outcome = "You win!"
        player_score += 1
    else:
        outcome = "Computer wins!"
        computer_score += 1
    
    # Print the outcome
    print(player_name, "Chose", player_choice, "Computer Chose", computer_choice)
    print(outcome)

# When the player ends the game, print the final scores and find the winner

print ("Final score of", player_name, "is", player_score)
print ("Final Score of Computer is", computer_score)

# Award the winner based on who has more points and print the result
if player_score > computer_score:
    print(player_name, "win!")
elif computer_score > player_score:
    print("Computer wins!")
else:
    print("It's a tie!")
