def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number == 1:
        return "Sunday"
    elif number == 2:
        return "Monday"
    elif number == 3:
        return "Tuesday"
    elif number == 4:
        return "Wednesday"
    elif number == 5:
        return "Thuraday"
    elif number == 6:
        return "Friday"
    elif number == 7:
        return "Saturday"

print(main(1))