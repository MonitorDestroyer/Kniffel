import random

def get_dice_roll() -> int:
    return random.randint(1, 6)

def initial_roll() -> list[int]:
    return [get_dice_roll() for __ in range(5)]

def reroll(roll: list[int], dice_to_reroll: int) -> None:
    roll[dice_to_reroll] = get_dice_roll()

def initial_card() -> list[int]:
    return [-1 for __ in range(13)]

def parse_result(result: int) -> str:
    match result:
        case -2:
            return "-"
        case -1:
            return ""
    return str(result)

def sum_upper_part(results: list[int]) -> int:
    sum = 0
    for i in range(6):
        if(results[i] >= 0):
            sum += results[i]
    return sum

def bonus_points(results: list[int]) -> int:
    if(sum_upper_part(results) >= 63):
        return 35
    return 0

def sum_lower_part(results: list[int]) -> int:
    sum = 0
    for i in range(6, 13):
        if(results[i] >= 0):
            sum += results[i]
    return sum