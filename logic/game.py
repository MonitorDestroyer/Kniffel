import random
from logic import constants

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

def sum_die(roll: list[int]) -> int:
    sum = 0
    for dice in roll:
        sum += dice
    return sum

def is_kniffel_general(roll: list[int]) -> int:
    if(roll[0] == roll[1] == roll[2] == roll[3] == roll[4]):
        return 50
    return -1

def is_kniffel(roll: list[int], results: list[int]) -> int:
    if(results[constants.KNIFFEL] == -2 or results[constants.KNIFFEL] == 50):
        return -1
    return is_kniffel_general(roll)

def is_three_of_a_kind_upper(roll: list[int], results: list[int], number: int) -> int:
    if(results[number - 1] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        sum: int = 0
        for dice in roll:
            if(dice == number):
                sum += number
        return sum
    return -1

def is_three_of_a_kind_lower(roll: list[int], results: list[int]) -> int:
    if(results[constants.THREE_OF_A_KIND] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        if(roll[0] == roll[1] == roll[2]):
            return sum_die(roll)
        if(roll[0] == roll[1] == roll[3]):
            return sum_die(roll)
        if(roll[0] == roll[1] == roll[4]):
            return sum_die(roll)
        if(roll[0] == roll[2] == roll[3]):
            return sum_die(roll)
        if(roll[0] == roll[2] == roll[4]):
            return sum_die(roll)
        if(roll[0] == roll[3] == roll[4]):
            return sum_die(roll)
        if(roll[1] == roll[2] == roll[3]):
            return sum_die(roll)
        if(roll[1] == roll[2] == roll[4]):
            return sum_die(roll)
        if(roll[1] == roll[3] == roll[4]):
            return sum_die(roll)
        if(roll[2] == roll[3] == roll[4]):
            return sum_die(roll)
    return -1

def is_four_of_a_kind(roll: list[int], results: list[int]) -> int:
    if(results[constants.FOUR_OF_A_KIND] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        if(roll[0] == roll[1] == roll[2] == roll[3]):
            return sum_die(roll)
        if(roll[0] == roll[1] == roll[2] == roll[4]):
            return sum_die(roll)
        if(roll[0] == roll[1] == roll[3] == roll[4]):
            return sum_die(roll)
        if(roll[0] == roll[2] == roll[3] == roll[4]):
            return sum_die(roll)
        if(roll[1] == roll[2] == roll[3] == roll[4]):
            return sum_die(roll)
    return -1

def get_individual_numbers(roll: list[int]) -> list[int]:
    individual_numbers: list[int] = [0 for __ in range(6)]
    for i in roll:
        individual_numbers[i - 1] = 1
    return individual_numbers

def is_small_street(roll: list[int], results: list[int]) -> int:
    if(results[constants.SMALL_STREET] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        individual_numbers: list[int] = get_individual_numbers(roll)
        if(individual_numbers[0] == individual_numbers[1] == individual_numbers[2] == individual_numbers[3] == 1):
            return 30
        if(individual_numbers[1] == individual_numbers[2] == individual_numbers[3] == individual_numbers[4] == 1):
            return 30
        if(individual_numbers[2] == individual_numbers[3] == individual_numbers[4] == individual_numbers[5] == 1):
            return 30
    return -1

def is_big_street(roll: list[int], results: list[int]) -> int:
    if(results[constants.SMALL_STREET] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        individual_numbers: list[int] = get_individual_numbers(roll)
        if(individual_numbers[0] == individual_numbers[1] == individual_numbers[2] == individual_numbers[3] == individual_numbers[4] == 1):
            return 40
        if(individual_numbers[1] == individual_numbers[2] == individual_numbers[3] == individual_numbers[4] == individual_numbers[5] == 1):
            return 40
    return -1

def get_individual_numbers_summed(roll: list[int]) -> list[int]:
    individual_numbers: list[int] = [0 for __ in range(6)]
    for i in roll:
        individual_numbers[i - 1] += 1
    return individual_numbers


def is_full_house(roll: list[int], results: list[int]) -> int:
    if(results[constants.SMALL_STREET] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        individual_numbers: list[int] = get_individual_numbers_summed(roll)
        has_two: bool = False
        has_three: bool = False
        for number in individual_numbers:
            if(number == 2):
                has_two = True
            elif(number == 3):
                has_three = True
        if(has_two == has_three == True):
            return 25
    return -1

def is_chance(roll: list[int], results: list[int]) -> int:
    if(results[constants.SMALL_STREET] == -1):
        if(results[constants.KNIFFEL] == 50 and is_kniffel_general(roll)):
            return 50
        return sum_die(roll)
    return -1