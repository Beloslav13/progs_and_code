def filter_list(my_list):
    """Фильтрует список."""
    _list = []
    for elem in my_list:
        if not isinstance(elem, str):
            _list.append(elem)
    return _list


# print(filter_list([1, 2, 'a', 'b']))
# print(filter_list([1, 'a', 'b', 0, 15]))
# print(filter_list([1, 2, 'aasf', '1', '123', 123]))


def find_it(number):
    """Найти нечетный int в списке."""
    for index, numb in enumerate(number):
        if number.count(numb) % 2 != 0:
            return numb


# print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
