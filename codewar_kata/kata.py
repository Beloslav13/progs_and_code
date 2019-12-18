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


# print(find_short("bitcoin take over the world maybe who knows perhaps"))


def accum(string):
    """Передай строку и сам всё увидишь."""
    value = ""
    for i, c in enumerate(string):
        value += c.upper() + c.lower() * i + "-"
    return value[:-1]


# print(accum("ZpglnRxqenU"))

def array_diff(a, b):
    """Удалить все значения из списка a, которые присутствуют в b."""
    for _ in a:
        if b:
            for numb_b in b:
                if a.count(numb_b):
                    a.remove(numb_b)
        else:
            return a
    return a


# print(array_diff(a=[1, 2, 2, 4], b=[1, 2, 3]))
# print(array_diff(a=[], b=[1, 2, 3]))


def order(strs):
    if not strs:
        return strs
    strs = strs.split()
    i = 1
    res = ''
    while i <= len(strs):
        for word in strs:
            if str(i) in word:
                res += word + ' '
                i += 1
    return res[:-1]


# print(order("is2 Thi1s T4est 3a"))
# print(order(""))


def namelist(names):
    len_names = len(names)
    i = 1
    res = ''
    for name in names:
        for n in name.items():
            if i == len_names - 1:
                res += n[1] + ' & '
            else:
                res += '' + n[1] + ', '
            i += 1
    return res[:-2]


# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))

