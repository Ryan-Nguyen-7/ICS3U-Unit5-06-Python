#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program uses rounds numbers
#   using passing by reference


def rounding(rounding_number, places):
    # rounds the decimal number

    rounding_number[0] = rounding_number[0] * (10 ** places) + 0.5

    rounding_number[0] = int(rounding_number[0])

    rounding_number[0] = rounding_number[0] / (10 ** places)


def main():
    # gets input and displays final output

    rounding_number = []

    temp_unrounded_as_string = input("Enter a number you would \
                                     like to round: ")
    places_as_string = input("Enter how many places you would \
                             like to round to: ")
    print("")

    # call function
    try:
        places_as_number = int(places_as_string)
        temp_unrounded_as_float = float(temp_unrounded_as_string)

        if places_as_number >= 0:
            rounding_number.append(temp_unrounded_as_float)
            rounding(rounding_number, places_as_number)

            # output
            final = rounding_number[0]

            print("Rounded decimal: {0}".format(final))
        else:
            print("Number of places must be positive")
    except Exception:
        print("Invalid unrounded number or number of places")


if __name__ == "__main__":
    main()
