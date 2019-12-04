class Analysis:
    """Класс анализирующий кол-во NOK в опеределенном промежутке времени."""

    def __init__(self, filename, write_path):
        self.filename = filename
        self.write_path = write_path
        self.stat = {}

    def read_file(self, write_path, numb):
        """Прочитать и создать словарь статистики по минутно."""
        with open(self.filename, 'r', encoding='utf8') as file:
            write_file = open(write_path, 'w', encoding='utf8')
            for line in file:
                char = line[1:numb]
                self.create_stat(line=line, char=char)
            self.write_stat(write_file)
            if write_file:
                write_file.close()

    def create_stat(self, line, char):
        """Записать в файл."""
        if 'NOK' in line:
            if char in self.stat:
                self.stat[char] += 1
            else:
                self.stat[char] = 1

    def write_stat(self, write_file):
        """Записать статистику"""
        for key, value in self.stat.items():
            write_file.write('[{}] '.format(key))
            write_file.write(str(value) + '\n')

    def start_methods(self):
        """Запуск методов"""
        self.read_file(write_path=self.write_path, numb=20)


class MinuteGroupFile(Analysis):

    def __init__(self, filename, write_path):
        super().__init__(filename=filename, write_path=write_path)

    def read_file(self, write_path, numb):
        super().read_file(write_path=write_path, numb=17)


class HoursGroupFile(Analysis):

    def __init__(self, filename, write_path):
        super().__init__(filename=filename, write_path=write_path)

    def read_file(self, write_path, numb):
        super().read_file(write_path=write_path, numb=14)


class MonthGroupFile(Analysis):

    def __init__(self, filename, write_path):
        super().__init__(filename=filename, write_path=write_path)

    def read_file(self, write_path, numb):
        super().read_file(write_path=write_path, numb=8)


class YearGroupFile(Analysis):

    def __init__(self, filename, write_path):
        super().__init__(filename=filename, write_path=write_path)

    def read_file(self, write_path, numb):
        super().read_file(write_path=write_path, numb=5)


minute_group_file = MinuteGroupFile(filename='events.txt', write_path='minute-group.txt')
minute_group_file.start_methods()

hour_group_file = HoursGroupFile(filename='events.txt', write_path='hour-group.txt')
hour_group_file.start_methods()

month_group_file = MonthGroupFile(filename='events.txt', write_path='month-group.txt')
month_group_file.start_methods()

year_group_file = YearGroupFile(filename='events.txt', write_path='year-group.txt')
year_group_file.start_methods()
