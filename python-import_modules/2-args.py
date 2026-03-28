#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # все аргументы кроме имени скрипта
    count = len(sys.argv) - 1

    # Первая строка с количеством аргументов
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Вывод каждого аргумента
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
