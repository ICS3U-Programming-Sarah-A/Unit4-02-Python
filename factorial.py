#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 20, 2022
# This program asks the user to enter a number. It then displays the factorial
# of the number the user entered using loops.


def main():
    # initialize the loop counter and factorial_answer
    loop_counter = 0
    factorial_answer = 1

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")

    try:
        # converts user input to integer
        user_number_int = int(user_number_string)
        # calculate the factorial of the user using loops.
        if user_number_int >= 0:
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                if loop_counter >= user_number_int:
                    break

            print("")
            print("{}! = {}".format(user_number_int, factorial_answer))

        else:
            print("{} is not a whole number".format(user_number_int))
    except Exception:
        print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()
