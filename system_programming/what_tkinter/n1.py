# Коды премеров находятся в функциях programm1 и programm2, а практическая в функции pracktika.
from tkinter import *

#Пример1
def programm1():
    def str_to_sort_list(event):
        s = ent.get()
        s = s.split()
        s.sort()
        lab['text'] = ' '.join(s)

    root = Tk()
    ent = Entry(root, width=20)
    but = Button(root, text="Преобразовать")
    lab = Label(root, width=20, bg='black', fg='white')
    but.bind('<Button-1>', str_to_sort_list)
    ent.pack()
    but.pack()
    lab.pack()
    root.mainloop()

#Пример2
def programm2():
    class Block:
        def __init__(self, master, func):
            self.ent = Entry(master, width=20)
            self.but = Button(master, text="Преобразовать")
            self.lab = Label(master, width=20, bg='black', fg='white')
            self.but['command'] = eval('self.' + func)
            self.ent.pack()
            self.but.pack()
            self.lab.pack()

        def str_to_sort_list(self):
            s = self.ent.get()
            s = s.split()
            s.sort()
            self.lab['text'] = ' '.join(s)

        def str_reverse(self):
            s = self.ent.get()
            s = s.split()
            s.reverse()
            self.lab['text'] = ' '.join(s)


    root = Tk()
    first_block = Block(root, 'str_to_sort_list')
    second_block = Block(root, 'str_reverse')
    root.mainloop()

#ПрактическаяРабота
def pracktika():
    def xz1():
        i1 = ent1.get()
        return int(i1)

    def xz2():
        i2 = ent2.get()
        return int(i2)

    def butt1(event):
        i = xz1() + xz2()
        i = str(i)
        lab['text'] = ' '.join(i)

    def butt2(event):
        print()
        i = xz1() - xz2()
        i = str(i)
        lab['text'] = ' '.join(i)

    def butt3(event):
        i = (xz1() * xz2())
        i = str(i)
        lab['text'] = ' '.join(i)

    def butt4(event):
        i = xz1() / xz2()
        i = str(i)
        lab['text'] = ' '.join(i)

    root = Tk()

    ent1 = Entry(root, width=20)
    ent2 = Entry(root, width=20)

    but1 = Button(root, text="+")
    but2 = Button(root, text="-")
    but3 = Button(root, text="*")
    but4 = Button(root, text="/")

    lab = Label(root, width=20, fg='black')

    but1.bind('<Button-1>', butt1)
    but2.bind('<Button-1>', butt2)
    but3.bind('<Button-1>', butt3)
    but4.bind('<Button-1>', butt4)

    ent1.pack()
    ent2.pack()

    but1.pack()
    but2.pack()
    but3.pack()
    but4.pack()

    lab.pack()

    root.mainloop()

#Код запуска программы, для проверки визуальной составляющей
def launch():
    a = input()
    if a == "Пример1":
        programm1()
    elif a == "Пример2":
        programm2()
    elif a == "ПрактическаяРабота":
        pracktika()
    else:
        print("Ошибка, неверные данные")
        return launch()

print('Что запустить, "Пример1", "Пример2", "ПрактическаяРабота"?')
launch()
input('Конец программы')