#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Return a new list with element replaced at idx without modifying original list."""
    # создаём копию списка
    new_list = my_list[:]
    # проверяем, что индекс корректный
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    # возвращаем новый список
    return new_list
