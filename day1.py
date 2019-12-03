#!/usr/bin/env python3

import os


FILENAME = 'day1input.txt'


def read_input(path):
    try:
        with open(path, 'r') as f:
            modules = f.readlines()
    except Exception as e:
        print(e)
    return modules


def calc_fuel(modules: list):
    sum = 0
    for item in modules:
        fuel = (int(item) // 3) - 2
        sum += fuel
    return sum


def main():
    modules = read_input(os.getcwd() + '/' + FILENAME)
    module_fuel = calc_fuel(modules)
    print(module_fuel)


if __name__ == "__main__":
    main()
