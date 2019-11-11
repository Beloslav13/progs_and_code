#!usr/bin/env python3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Создать файл')
root.geometry('400x300')

inf = Button(text='Что делать?', command=lambda: infs())
file_name_title = Label(text='Название файла:')
file_name = Entry()
file_write_title = Label(text='Что записываем (не обязательное):')
file_write = Entry()
btn = Button(text='Создать', width='15', command=lambda: write())


def infs():
    messagebox.showinfo('Программа для создания файлов',
                        'Можно создать файл и записать в него первые строки. Если расширение файла не указано, '
                        'по умолчанию файл создаеся как текстовый.')


def write():
    try:
        file_open = open(file_name.get(), 'w')
        file_open.write(file_write.get())
        file_open.close()
        file_name.delete(0, END)
        file_write.delete(0, END)
        messagebox.showinfo('Завершено', 'Создание файла завершено')
    except:
        messagebox.showerror('Ошибка', 'Давай не шали, введи то, что просят!')


inf.pack()
file_name_title.pack()
file_name.pack()
file_write_title.pack()
file_write.pack()
btn.pack()

root.mainloop()
