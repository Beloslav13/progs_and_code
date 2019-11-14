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


def getCount(input_str):
    """Возвращает кол-во гласных(пример)"""
    num_vowels = 0
    chars = 'aeiou'
    for index, char_input in enumerate(input_str):
        for char in chars:
            if char == char_input:
                num_vowels += 1
    return num_vowels


# print(getCount("abracadabra"))

def my_numbers(chars):
    """Возвращает номера строк"""
    template = []
    for index, char in enumerate(chars):
        index = index + 1
        template.append(str(index) + ': ' + char)
    return template


# print(my_numbers(["a", "b", "c"]))

def find_short(s):
    """Возвращает длину самого короткого слова в строке."""
    template = []
    words = s.split()
    for word in words:
        word_len = len(word)
        template.append(word_len)
    return min(template)


print(find_short("bitcoin take over the world maybe who knows perhaps"))