# Reads the dices data inputs


def dice_reader():
    dice_expression: str = input("Enter the roll in the format: <#dices>d<#faces><+/-><modifier>\n>> ")
    dice = dice_expression.split('d')

    if '-' in dice[1]:
        dice[1] = dice[1].replace('-', '+-')
    if '+' in dice[1]:
        dice += dice[1].split('+')
        dice.remove(dice[1])
    else:
        dice.append(0)

    try:
        n, f, m = map(int, dice)
    except ValueError:
        print("Invalid format or values. Please, try again.")
        dice_reader()
    else:
        return n, f, m


def sum_reader():
    try:
        s = int(input("What result do you want?\n>>> "))
    except ValueError:
        print("Please, enter a integer number.")
        sum_reader()
    else:
        return s


def sum_comparator_reader():
    range_text = input("The sum must be: [>INTEGER] ")
    goal = str()  # Before it will be integer
    operator = str()

    try:
        for char in range_text:
            if char in "><":
                operator += char
            elif char.isdigit():
                goal += char
            else:
                raise ValueError("Invalid input. Please, try again.")
    except ValueError:
        return sum_comparator_reader()

    try:
        s = int(goal)
    except ValueError:
        print("Please, enter a integer number.")
        sum_comparator_reader()
    else:
        return operator, s