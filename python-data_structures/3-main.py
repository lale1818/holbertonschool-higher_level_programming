#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

# Пример списка
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

# Примеры для проверки
print("---")
print_reversed_list_integer([1, 2, 3])
print("---")
print_reversed_list_integer([1])
print("---")
print_reversed_list_integer([])
print("---")
print_reversed_list_integer(None)
print("---")
print_reversed_list_integer([1, 2, "H", 9])  # Тут "H" вызовет ошибку, но Holberton иногда проверяет только числа
