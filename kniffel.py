from logic import game
from logic import constants
from output import console

def main() -> None:
    roll: list[int] = game.initial_roll()
    player_one: list[int] = game.initial_card()
    player_two: list[int] = game.initial_card()
    current_player: int = 1
    rerolls_left: int = 2

    print(game.is_full_house([5, 5, 3, 5, 2], player_one))

if(__name__ == "__main__"):
    main()