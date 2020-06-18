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
    """Расставить слова по числам."""
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
    """Добавить & перед последним именем."""
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


def count(string):
    """Кол-во символов в переданной строке."""
    my_dict = {}
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


# print(count('aba'))
# # print(count(''))


def remove_smallest(numb):
    """Удалить наименьшее число без изменения входных данных"""
    if numb:
        numb_copy = numb.copy()
        min_numb = min(numb_copy)
        numb_copy.remove(min_numb)
        return numb_copy
    return numb


# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# print(remove_smallest([5, 3, 2, 1, 4]))
# print(remove_smallest([]))

def digitize(n):
    """Convert number to reversed array of digits"""
    res = list(str(n))
    res.reverse()
    return list(map(int, res))


def find_it_two(seq):
    """Find the odd int"""
    return set([char for char in seq if seq.count(char) % 2 != 0]).pop()


def unique_in_order(iterable):
    """Unique In Order"""
    char = []
    i = 0
    for ch in iterable:
        if i < 1:
            char.append(ch)
        elif ch != iterable[i - 1]:
            char.append(ch)
        i += 1
    return char


def sort_array(my_list):
    """Sorting odd numbers"""
    odds = sorted((x for x in my_list if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in my_list]


def digital_root(n):
    """Sum of Digits / Digital Root"""
    if n < 10:
        return n
    new = sum([int(numb) for numb in str(n)])
    return digital_root(n=new)


def find_outlier(integers):
    """Find The Parity Outlier"""
    add = [numb for numb in integers if not numb % 2]
    for numb in integers:
        if len(add) == 1:
            return add[0]
        else:
            if numb % 2:
                return numb


def order_weight(strng):
    """
    Sorting numbers by their weight.

    Example:
        strng = '103 123 4444 99 2000'
        weight = 103 -> 4 (1 + 0 + 3), 123 -> 6 (1 + 2 + 3)
        return = '2000 103 123 4444 99'
    """
    list_numb_split = [numb for numb in strng.split()]
    list_numb_tuple = []
    result = ''
    for numb in list_numb_split:
        res_sum = sum(map(int, list(numb)))
        tup = (numb, res_sum)
        list_numb_tuple.append(tup)
    re = sorted(list_numb_tuple, key=lambda item: (item[1], item[0]))
    for r in re:
        result += r[0] + ' '
    return result[:-1]


# print(order_weight(strng='103 123 4444 99 2000'))


def anagrams(word, words):
    """
    :param word: 'abba'
    :param words: ['aabb', 'abcd', 'bbaa', 'dada']
    :return: ['aabb', 'bbaa']
    """
    count_char = {}
    count_char_word = {}
    result = []
    for char in word:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1

    for key, value in count_char.items():
        for w in words:
            if len(word) != len(w):
                continue
            if w in count_char_word:
                count_char_word[w].update({key: w.count(key)})
            else:
                count_char_word[w] = {key: w.count(key)}

    for key, value in count_char_word.items():
        if count_char_word[key] == count_char:
            result.append(key)
    return result
