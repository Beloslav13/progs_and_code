from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Виртуальный ребёнок')


def que():
    title = Label(root, text='Знакомтесь, это виртуальный ребёнок Кеша, который очень любит вопрос "Почему?"')
    title.grid(row=0)
    question = Label(root, text='Почему?')
    question.grid(row=1)
    answer = Entry()
    answer.grid(row=2)
    btn = ttk.Button(root, text='Ответить', command=lambda: child(que))
    btn.grid(row=3)

    def child(que):
        if answer.get().lower() == 'потому что':
            messagebox.showinfo('Ура', 'Вы победили виртуального ребёнка, ответ оказался верным')
            # exit()
        else:
            messagebox.showerror('Неверно', 'К сожалению вы ввели не верное значение, попробуйте еще раз!')
            que()


que()
root.mainloop()
