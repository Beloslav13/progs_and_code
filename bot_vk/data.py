
words_weather = ['погода', 'узнать погоду']


def create_list_city():
    cities = []
    with open('cities.csv', 'r', encoding='utf8') as file:
        for line in file:
            line = line.strip()
            cities.append(line.lower())
    return cities


if __name__ == '__main__':
    print(create_list_city())
