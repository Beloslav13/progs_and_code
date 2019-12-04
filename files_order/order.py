import os, time, shutil


class FileOrder:

    def __init__(self, path):
        self.path = path

    def walk_dir(self):
        """Просканировать директории."""
        for dirpath, dirname, filename in os.walk(self.path):
            for file in filename:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                dates = self.optimaze_file_time(file_time=file_time)
                self.create_dir(dates=dates, path='icons_by_year')
                self.copy_file(dates=dates, full_file_path=full_file_path)

    def optimaze_file_time(self, file_time):
        """Поменять формат месяца."""
        if len(str(file_time[1])) < 2:
            file_time_res = '0' + str(file_time[1])
        else:
            file_time_res = str(file_time[1])
        dates = str(file_time[0]) + '/' + file_time_res
        return dates

    def create_dir(self, dates, path):
        """Создать директории."""
        os.makedirs(os.path.join(path, dates), exist_ok=True)

    def copy_file(self, dates, full_file_path):
        """Скопировать файлы."""
        path_copy_norm = os.path.normpath(os.path.join('icons_by_year', dates))
        shutil.copy2(full_file_path, path_copy_norm)


path = 'icons'
path_norm = os.path.normpath(path)
file_order = FileOrder(path=path_norm)
file_order.walk_dir()
