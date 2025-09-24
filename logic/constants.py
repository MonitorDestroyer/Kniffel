ONES: int = 0
TWOS: int = 1
THREES: int = 2
FOURS: int = 3
FIVES: int = 4
SIXES: int = 5
THREE_OF_A_KIND: int = 6
FOUR_OF_A_KIND: int = 7
FULL_HOUSE: int = 8
SMALL_STREET: int = 9
BIG_STREET: int = 10
KNIFFEL: int = 11
CHANCE: int = 12

def index_to_name(index: int) -> str:
    match index:
        case 0:
            return "Ones"
        case 1:
            return "Twos"
        case 2:
            return "Threes"
        case 3:
            return "Fours"
        case 4:
            return "Fives"
        case 5:
            return "Sixes"
        case 6:
            return "Three of a kind"
        case 7:
            return "Four of a kind"
        case 8:
            return "Small street"
        case 9:
            return "Big street"
        case 10:
            return "Full house"
        case 11:
            return "Kniffel"
        case 12:
            return "Chance"
    return "?"