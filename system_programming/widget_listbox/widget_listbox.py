from tkinter import *

def example1():
    root = Tk()

    lb = Listbox(width=15, height=8)
    lb.pack()

    for i in ('one','two','tree','four','six','seven'):
        lb.insert(0,i)

    root.mainloop()
#-----------------------------------------------------------------
#Второй пример был дополнен, чтобы кнопка Save имела смысл, чтобы можно не только сохранять, но и загружать.
def example2():
    def add_item():
        box.insert(END, entry.get())
        entry.delete(0, END)

    def del_list():
        select = list(box.curselection())
        select.reverse()
        for i in select:
            box.delete(i)

    def save_list():
        f = open('list000.txt', 'w')
        f.writelines("\n".join(box.get(0, END)))
        f.close()

    def load_list():
        l = open('list000.txt')
        text_load = l.readlines()
        for i in text_load:
            box.insert(END, i)

    root = Tk()

    box = Listbox(selectmode=EXTENDED)
    box.pack(side=LEFT)
    scroll = Scrollbar(command=box.yview)
    scroll.pack(side=LEFT, fill=Y)
    box.config(yscrollcommand=scroll.set)

    f = Frame()
    f.pack(side=LEFT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    Button(f, text="Add", command=add_item).pack(fill=X)
    Button(f, text="Delete", command=del_list).pack(fill=X)
    Button(f, text="Save", command=save_list).pack(fill=X)
    Button(f, text="Load", command=load_list).pack(fill=X)

    root.mainloop()

#--------------------------------------------------------------
def practical():
    list_purchase = ['apple', 'bananas','bread', 'butter', 'carrot', 'meat', 'milk', 'pineapple', 'potato', 'tomato']

    def push_right():
        select = list(lb1.curselection())
        select.reverse()
        for i in select:
            lb2.insert(END, lb1.get(i))
            lb1.delete(i)

    def push_left():
        select = list(lb2.curselection())
        select.reverse()
        for i in select:
            lb1.insert(END, lb2.get(i))
            lb2.delete(i)

    root = Tk()
    lb1 = Listbox(selectmode=EXTENDED)
    for i in list_purchase:
        lb1.insert(END, i)
    lb2 = Listbox(selectmode=EXTENDED)

    f = Frame()

    Button(f, text=">>>", command=push_right).pack(fill=X)
    Button(f, text="<<<", command=push_left).pack(fill=X)

    lb1.pack(side = LEFT)
    f.pack(side = LEFT)
    lb2.pack(side = LEFT)
    root.mainloop()
#------------------------------------------------------------------
print("Введите одну из цифр: 1 - Первый пример, 2 - Второй пример, 3 - Практическая работа")
a = input()
if a == '1':
    example1()
elif a == '2':
    example2()
elif a == '3':
    practical()
else: print('Введено не правельное значение')