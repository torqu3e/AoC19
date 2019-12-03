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
    fuel_per_module = []
    for item in modules:
        fuel = int(item) // 3 - 2
        sum = fuel
        while fuel >= 6:
            more_fuel = (int(fuel) // 3) - 2
            fuel = more_fuel
            sum += more_fuel
        fuel_per_module.append(sum)
    return fuel_per_module


def main():
    modules = read_input(os.getcwd() + '/' + FILENAME)
    module_fuel = calc_fuel(modules)
    print(sum(module_fuel))


if __name__ == "__main__":
    main()
