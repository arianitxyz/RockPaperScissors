import random
import re  # regex to check if the player input is in the regex
import os


def check_play():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input("Do you want to play again> Yes / No\n")
            if response.casefold() not in valid_responses:
                raise ValueError("Yes or No only!")
            if response.casefold() == "yes":
                return True
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Thanks for playing")
                exit()

        except ValueError as error:
            print(error)


def play_rps():
    choices = ["r", "p", "s", ]
    play = True

    while play:
        player_choice = input(print_possible_choices())

        if not re.match("[RrSsPp]", player_choice):
            print_possible_choices()
            continue
        print_choice("Player", player_choice)

        comp_choice = random.choice(choices)
        print_choice("Computer", comp_choice)

        play = validate_game(comp_choice, player_choice)


def print_choice(player: str, player_input: str) -> str:
    print(f"{player}s choice was ", player_input)


def print_possible_choices():
    return "Please input one of the options for your move: \n R. Rock \n P. Paper \n S. Scissors\n"


def validate_game(comp_choice, player_choice):
    if player_choice == comp_choice:
        print("Tie since both players chose ", player_choice)
        play = check_play()
    elif comp_choice == 'r' and player_choice == 's':
        print_game_result("Computer", comp_choice, player_choice)
        play = check_play()
    elif comp_choice == 's' and player_choice == 'p':
        print_game_result("Computer", comp_choice, player_choice)
        play = check_play()
    elif comp_choice == 'p' and player_choice == 'r':
        print_game_result("Computer", comp_choice, player_choice)
        play = check_play()
    else:
        print_game_result("Player", player_choice, comp_choice)
        play = check_play()
    return play


def print_game_result(winner: str, winner_input: str, loser_input: str):
    print(f"{winner} wins since {winner_input} beats {loser_input}")


play_rps()
