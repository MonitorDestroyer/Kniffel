from logic import game
from output import console

def main() -> None:
    roll: list[int] = game.initial_roll()
    player_one: list[int] = game.initial_card()
    player_two: list[int] = game.initial_card()
    current_player: int = 1
    rerolls_left: int = 2

    console.print_game_state(player_one, player_two, roll, current_player, rerolls_left)



if(__name__ == "__main__"):
    main()