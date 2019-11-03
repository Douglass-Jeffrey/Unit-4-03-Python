#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program squares and displays all previously occuring integers


def main():
    # funciton calculates value_1 squared

    # variable
    answer = 1
    looper = 0
    try:
        # input
        value_1 = int(input("What is your number: "))

        # process
        for looper in range(value_1 + 1):
            answer = looper * looper
            print(str(looper) + "² = " + str(answer))
    except Exception:
        print("Please input a proper integer")


if __name__ == "__main__":
    main()
