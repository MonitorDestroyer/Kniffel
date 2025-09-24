from output import constants
from output.table import Table
from logic import constants as cnst
from logic import game

def print_game_state(player_one: list[int], player_two: list[int], roll: list[int], current_player: int, rerolls_left: int) -> None:
    table: Table = Table("Game State")
    table.add_column(25, "Category", constants.ALIGN_LEFT)
    table.add_column(12, "Player One", constants.ALIGN_CENTER)
    table.add_column(12, "Player Two", constants.ALIGN_CENTER)

    for i in range(6):
        table.add_row([cnst.index_to_name(i), game.parse_result(player_one[i]), game.parse_result(player_two[i])])

    sum_upper_one: int = game.sum_upper_part(player_one)
    bonus_one: int = game.bonus_points(player_one)
    sum_upper_full_one: int = sum_upper_one + bonus_one

    sum_upper_two: int = game.sum_upper_part(player_two)
    bonus_two: int = game.bonus_points(player_two)
    sum_upper_full_two: int = sum_upper_two + bonus_two

    table.add_row(["Sum", str(sum_upper_one), str(sum_upper_two)])
    table.add_row(["Bonus(63 or more)", str(bonus_one), str(bonus_two)])
    table.add_row(["Sum upper part", str(sum_upper_full_one), str(sum_upper_full_two)])

    for i in range(6, 13):
        table.add_row([cnst.index_to_name(i), game.parse_result(player_one[i]), game.parse_result(player_two[i])])

    sum_lower_one: int = game.sum_lower_part(player_one)
    sum_full_one: int = sum_upper_full_one + sum_lower_one

    sum_lower_two: int = game.sum_lower_part(player_two)
    sum_full_two: int = sum_upper_full_two + sum_lower_two

    table.add_row(["Sum lower part", str(sum_lower_one), str(sum_lower_two)])
    table.add_row(["Sum total", str(sum_full_one), str(sum_full_two)])

    table.print_table()

def print_roll(roll: list[int]) -> None:
    roll_output: str = ""
    i: int = 1
    for dice in roll:
        roll_output += f"[{dice}]"
        if(i < 5):
            roll_output += " "
        i += 1
    print(roll_output)