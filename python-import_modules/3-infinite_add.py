#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # аргументы кроме имени скрипта
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
