import random


def replay(response: str) -> bool:
    valid_responses = ['yes', 'no']

    if response.casefold() not in valid_responses or response.casefold() == 'no':
        return False
    if response.casefold() == "yes":
        return True


def validate(player: str, opponent: str) -> str:
    if player == opponent:
        return f'nobody wins {player} = {opponent}'
    elif opponent == 'r' and player == 's':
        return f'opponent wins: {opponent} > {player}'
    elif opponent == 's' and player == 'p':
        return f'opponent wins: {opponent} > {player}'
    elif opponent == 'p' and player == 'r':
        return f'opponent wins: {opponent} > {player}'
    else:
        return f'player wins: {player} > {opponent}'


def play(player: str, opponent: str, is_random: bool) -> str:
    options = ['r', 'p', 's']
    if is_random:
        player = random.choice(options)
        opponent = random.choice(options)
    return validate(player, opponent)


def play_with_computer(player: str, is_random: bool) -> str:
    options = ['r', 'p', 's']
    if is_random:
        opponent = random.choice(options)
    return validate(player, opponent)


def play():
    options = ['r', 'p', 's']
    is_playing = True
    while is_playing:
        player = str(input('Enter r p s '))
        if player in options:
            print(play_with_computer(player, True))
            is_playing = replay(input('Play again?'))
        else:
            continue
