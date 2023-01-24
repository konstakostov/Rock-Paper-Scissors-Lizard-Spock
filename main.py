import random   # Random Number Generator
from colorama import Fore, Style    # Adds color to the text

print("Hello, this is 'Rock, Paper, Scissors, Lizard, Spock!'. The rules of the game are:")
print("Scissors cut Paper. Paper covers Rock. Rock crushes Lizard. Lizard poisons Spock. Spock smashes Scissors")
print("Scissors decapitate Lizard. Lizard eats Paper. Paper disproves Spock. Spock vaporizes Rock.")
print("And as everybody knows - Rock crushes Scissors.")
print()
print("Please, enter your name: ")
name = input()  # Player Name

# Variables, for each of the legal choices
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
lizard = "Lizard"
spock = "Spock"

# Counter for rounds and Win/Loss/Draw ratio
rounds = 1
wins = 0
losses = 0
draws = 0

new_game = ""

# Main Logic
while new_game == "" or new_game == "y":
    print(f"Round {rounds}. Start!")
    print(f"Wins: {wins}    Losses: {losses}    Draws: {draws}")
    print("Rock --> 'r'   Paper --> 'p'   Scissors --> 'sc'   Lizard --> 'l'   Spock --> 'sp'")

    player_input = ""

    # This loops reads the player choice about his input for the game
    # If the player's choice is not a legal choice it prompts him to try again
    # The loop does not end until a legal choice has been made by the player
    while player_input != "r" or player_input != "p" or \
            player_input != "s" or player_input != "l" or player_input != "s":

        player_input = input()

        if player_input == "r":
            player_input = rock
            break
        elif player_input == "p":
            player_input = paper
            break
        elif player_input == "sc":
            player_input = scissors
            break
        elif player_input == "l":
            player_input = lizard
            break
        elif player_input == "sp":
            player_input = spock
            break
        else:
            print("Invalid choice. Please, try again.")

    # The computers choice is being made by a random number generator in (1, 5) range
    computer_input = ""
    computer_rand_num = random.randint(1, 5)

    if computer_rand_num == 1:
        computer_input = rock
    elif computer_rand_num == 2:
        computer_input = paper
    elif computer_rand_num == 3:
        computer_input = scissors
    elif computer_rand_num == 4:
        computer_input = lizard
    elif computer_rand_num == 5:
        computer_input = spock

    print(f"{name} has played {player_input} and the Computer has played {computer_input}")

    # Logic for the different scenarios depending on the players and the computers input

    # Rock Wins Scenarios
    if player_input == rock and (computer_input == scissors or computer_input == lizard):   # Player Wins
        print(f"{player_input} crushes {computer_input}.")
        print(Fore.GREEN + "You Win!")
        wins += 1
    elif computer_input == rock and (player_input == scissors or player_input == lizard):   # Computer Wins
        print(f"{player_input} crushes {computer_input}.")
        print(Fore.RED + "You Lose!")
        losses += 1

    # Paper Wins Scenarios
    elif player_input == paper and (computer_input == rock or computer_input == spock):   # Player Wins
        if computer_input == rock:
            print(f"{player_input} covers {computer_input}.")
        elif computer_input == spock:
            print(f"{player_input} disproves {computer_input}.")
        print(Fore.GREEN + "You Win!")
        wins += 1
    elif computer_input == paper and (player_input == rock or player_input == spock):   # Computer Wins
        if player_input == rock:
            print(f"{computer_input} covers {player_input}.")
        elif player_input == spock:
            print(f"{computer_input} disproves {player_input}.")
        print(Fore.RED + "You Lose!")
        losses += 1

    # Scissors Wins Scenarios:
    elif player_input == scissors and (computer_input == paper or computer_input == lizard):   # Player Wins
        if computer_input == paper:
            print(f"{player_input} cut {computer_input}.")
        elif computer_input == lizard:
            print(f"{player_input} decapitate {computer_input}.")
        print(Fore.GREEN + "You Win!")
        wins += 1
    elif computer_input == scissors and (player_input == paper or player_input == lizard):   # Computer Wins
        if player_input == paper:
            print(f"{computer_input} cut {player_input}.")
        elif player_input == lizard:
            print(f"{computer_input} decapitate {player_input}.")
        print(Fore.RED + "You Lose!")
        losses += 1

    # Lizard Wins Scenarios:
    elif player_input == lizard and (computer_input == spock or computer_input == paper):   # Player Wins
        if computer_input == spock:
            print(f"{player_input} poisons {computer_input}.")
        elif computer_input == paper:
            print(f"{player_input} eats {computer_input}.")
        print(Fore.GREEN + "You Win!")
        wins += 1
    elif computer_input == lizard and (player_input == spock or player_input == paper):   # Computer Wins
        if player_input == spock:
            print(f"{computer_input} poisons {player_input}.")
        elif player_input == paper:
            print(f"{computer_input} eats {player_input}.")
        print(Fore.RED + "You Lose!")
        losses += 1

    # Spock Wins Scenarios:
    elif player_input == spock and (computer_input == scissors or computer_input == rock):   # Player Wins
        if computer_input == scissors:
            print(f"{player_input} smashes {computer_input}.")
        elif computer_input == rock:
            print(f"{player_input} vaporizes {computer_input}.")
        print(Fore.GREEN + "You Win!")
        wins += 1
    elif computer_input == lizard and (player_input == spock or player_input == paper):   # Computer Wins
        if player_input == scissors:
            print(f"{computer_input} smashes {player_input}.")
        elif player_input == rock:
            print(f"{computer_input} vaporizes {player_input}.")
        print(Fore.RED + "You Lose!")
        losses += 1

    # Scenarios where both inputs result in a draw
    else:
        print(Fore.BLUE + "It's a Draw!")
        draws += 1

    print(Style.RESET_ALL)

    # Logic determining whether the game will continue or not
    print("Do you want to play a new game?")
    new_game = ""

    # This loops reads the player choice to continue the game or not.
    # If the player's choice is not a legal choice it prompts him to try again
    # The loop does not end until a legal choice has been made by the player
    while new_game != "y" or new_game != "q":
        new_game = input("'y' for new game and 'q' to quit: ")
        if new_game == "q":
            break
        elif new_game == "y":
            rounds += 1
            break
        else:
            print("Invalid input. Please, try again.")

# Final statistics for the game the player has played
print(f"{name}, you played {rounds} rounds.")
print(f"You have won {wins}, lost {losses} and {draws} resulted in a draw.")
