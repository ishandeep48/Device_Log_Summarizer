import math
from math import inf, nan


def clean_readings(readings):
    """
    Clean and normalize sensor readings.
    Takes the readings in a list then keeps the values that are positive and converts then to float .
    also if any value is greater than 500 then caps it at 500 . doesnt keep other values
    nan is removed 
    inf is converted to 500.0

    Examples:
        >>> clean_readings([25, "30.5", None, -10, "ERROR", 600, 45])
        [25.0, 30.5, 500.0, 45.0]

        >>> clean_readings([])
        []

        >>> clean_readings([None, -5, "abc"])
        []

        >>> clean_readings([float('nan'), nan, 20, float('nan')])
        [20.0]

        >>> clean_readings([float('inf'), -inf, float('-inf'), 25])
        [500.0, 25.0]
    """

    cleaned = []

    for value in readings:
        try:
            number = float(value)
        except (ValueError, TypeError, OverflowError):
            continue

        if math.isnan(number) or number < 0:
            continue

        if number > 500.0:
            number = 500.0

        cleaned.append(number)

    return cleaned