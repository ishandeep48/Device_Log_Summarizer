# import doctest
# from sanitizer import clean_readings


# if __name__ == "__main__":
#     doctest.testmod(verbose=True)

#     # please put the values yoyu wanna test here
#     readings = [25, "30.5", None, -10, "ERROR", 600]

#     print("\nCustom test:")
#     print(clean_readings(readings))

from sanitizer import clean_readings


def main():
    print("=== Sensor Readings Sanitizer ===")
    print("Enter comma-separated sensor readings.")
    print("Example: 25, 30.5, None, -10, ERROR, 600")

    user_input = input("\nReadings: ")

    readings = [
        value.strip() for value in user_input.split(",")
    ]

    print("\nOriginal readings:")
    print(readings)

    cleaned = clean_readings(readings)

    print("\nCleaned readings:")
    print(cleaned)

    print(f"\n{len(cleaned)} valid readings retained.")


if __name__ == "__main__":
    main()