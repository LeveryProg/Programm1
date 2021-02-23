from tkinter import *
from datetime import datetime

def YeasOrNot():
    a = input('>')
    if a == 'Y' or a == 'y':
        return 'true'
    elif a == 'N' or a == 'n':
        return 'false'
    else:
        print("Введите корректное значение:")
        return YeasOrNot()

def Filtration(englishWord, russianWord, transcription, pronunciationBritish, pronunciationAmerican, synonym,
                   lifeHack, definition1, definition2, definition3):
    global text1
    global text2
    global text3
    global text4

    #text1
    if englishWord == "" and transcription == "" and russianWord == "" and synonym == "":
        text1 = "Отсутствует текст"

    elif englishWord != "" and transcription != "" and russianWord != "" and synonym != "":
        text1 = englishWord + transcription + "\n - " + russianWord + ": " + synonym + "."

    elif englishWord == "" or russianWord == "":
        text1 = "Некоректный текст"

    elif synonym == "":
        text1 = englishWord + transcription + "\n - " + russianWord + "."

    elif transcription == "":
        text1 = englishWord +  " - " + russianWord + ":\n" + synonym + "."

    elif englishWord != "" and russianWord != "":
        text1 = englishWord + " - " + russianWord + "."

    else:
        text1 = "Ошибка, недопустимое значение"

    #text2
    if pronunciationBritish != "" and pronunciationAmerican != "":
        text2 = pronunciationBritish +";\n"+ pronunciationAmerican +"."

    elif pronunciationBritish == "" and pronunciationAmerican == "":
        text2 = "Отсутствует текст"

    elif pronunciationAmerican == "":
        text2 = pronunciationBritish + "."

    elif pronunciationBritish == "":
        text2 = pronunciationAmerican + "."

    else:
        text2 = "Ошибка, недопустимое значение"

    #text3
    if definition1 == "" and definition2 == "" and definition3 == "":
        text3 = "Отсутствует текст"
    else:
        text3 = definition1 +"\n"+ definition2 +"\n"+ definition3

    #text4
    text4 = lifeHack

def ReadingWithFilter(txtName):
    readingWords = open(txtName, 'r', encoding='utf-8')
    t1 = readingWords.readline() #Слово на английском
    t2 = readingWords.readline() #Слово на русском
    t3 = readingWords.readline() #Транскрипция
    t4 = readingWords.readline() #Произношение Бр
    t5 = readingWords.readline() #Произношение Ам
    t6 = readingWords.readline() #Синоним
    t7 = readingWords.readline() #Как запомнить
    t8 = readingWords.readline() #Определение
    t9 = readingWords.readline() #Определение
    t10 = readingWords.readline()#Определение
    Filtration(t1[:-1],t2[:-1],t3[:-1],t4[:-1],t5[:-1],t6[:-1],t7[:-1],t8[:-1],t9[:-1],t10[:-1])
    readingWords.close()

def Recreating():
    root = Tk()
    root.title("Word of The Day")
    c = Canvas(root, width=300, height=150, bg='brown')
    c.pack()
    c.create_rectangle(5, 5, 296, 146, fill='white')
    c.create_text(150,30, text=text1, font=("Verdana", 10, 'bold'))
    c.create_text(150,65, text=text2, font="Verdana 10")
    c.create_text(150,100, text=text3, font=("Verdana", 8, 'italic'))
    c.create_text(220, 140, text=text4, fill='grey')
    root.mainloop()

def ReaderAndWriter(nameInputFile, nameOutputFile):
    readFile = open(nameInputFile, 'r', encoding='utf-8')
    textReadedFile = readFile.readlines()
    writeFile = open(nameOutputFile, 'w', encoding='utf-8')
    writeFile.writelines(textReadedFile)
    readFile.close()
    writeFile.close()

def Deleter(whatDelete):
    removable = open(whatDelete, 'w', encoding='utf-8')
    removable.writelines("")
    removable.close()

def Addition(whatAdd):
    print("Введите, слово на английское:")
    textBlock1 = input('>')
    print("Введите, слово на руском:")
    textBlock2 = input('>')
    print("Введите, транскрипцию:")
    textBlock3 = input('>')
    print("Введите, произношение на британский манер:")
    textBlock4 = input('>')
    print("Введите, произношение на амереканский манер:")
    textBlock5 = input('>')
    print("Введите, синоним:")
    textBlock6 = input('>')
    print("Введите, как можно запомнить это слово:")
    textBlock7 = input('>')
    print("Введите, Описание 1:")
    textBlock8 = input('>')
    print("Введите, Описание 2:")
    textBlock9 = input('>')
    print("Введите,: Описание 3")
    textBlock10 = input('>')
    texted = textBlock1 + "\n" + textBlock2 + "\n[" + textBlock3 + "]\nБр: " + textBlock4 +"\nАм: "+ textBlock5 +"\n"+ \
             textBlock6 +"\n"+textBlock7+"\n"+textBlock8+"\n"+textBlock9+"\n"+textBlock10
    add = open(whatAdd, 'w', encoding='utf-8')
    add.writelines(texted)
    add.close()

def NewDayHorizon():

#Этап 1
    print("\nВы хотите, сохранить копию слово позавчерешнего дня? Y/N")
    stage1 = YeasOrNot()
    if stage1 == 'true':
        dtime = datetime.now()
        time = str(dtime.year) + '.' + str(dtime.month) + '.' + str(dtime.day) + ' ' + str(dtime.hour) + '.' + str(
            dtime.minute) + '.' + str(dtime.second) + '.txt'
        ReaderAndWriter('wotdTDBY.txt', time)
        print("Созданна копия файла с позавчерашним словом дня!")
    elif stage1 == 'false':
        print("Копия не была создана!")
    else:
        print("Ошибка, в мотоде YeasOrNot")
#Этап 2
    print("\nВы хотите, обновить позавчерашние слово дня? Y/N")
    stage2 = YeasOrNot()
    if stage2 == 'true':
        ReaderAndWriter('wotdYesterday.txt', 'wotdTDBY.txt')
        print("Позавчерашние слово дня, было обновлено!")
    elif stage2 == 'false':
        print("Позавчерашние слово дня, не было обновлено!")
    else:
        print("Ошибка, в мотоде YeasOrNot")
#Этап 3
    print("\nВы хотите, обновить вчерашние слово дня? Y/N")
    stage3 = YeasOrNot()
    if stage3 == 'true':
        ReaderAndWriter('wotdToday.txt','wotdYesterday.txt')
        print("Вчерашние слово дня, было обновлено!")
    elif stage3 == 'false':
        print("Вчерашние слово дня, не было обновлено!")
    else:
        print("Ошибка, в мотоде YeasOrNot")
#Этап 4
    print("\nВы хотите, очистить слово сегодняшнего дня? Y/N")
    stage4 = YeasOrNot()
    if stage4 == 'true':
        Deleter('wotdToday.txt')
        print("Слово сегодняшнего дня, удалено!")
    elif stage4 == 'false':
        print("Слово сегодняшнего дня, не удалено!")
    else:
        print("Ошибка, в мотоде YeasOrNot")
#Этап 5
    print("\nВы хотите, добавить слово дня? Y/N")
    stage5 = YeasOrNot()
    if stage5 == 'true':
        Addition('wotdToday.txt')
        print("Слово сегодняшнего дня, добавлено!")
    elif stage5 == 'false':
        print("Слово сегодняшнего дня, не добавлено!")
    else:
        print("Ошибка, в мотоде YeasOrNot")

def Launch():
    print("Введите цифру, чтобы выбрать: слово дня(1), предыдущего дня(2) или позопрошлого дня(3):")
    iN = input('>')
    if iN == '1':
        ReadingWithFilter('wotdToday.txt')
        Recreating()
    elif iN == '2':
        ReadingWithFilter('wotdYesterday.txt')
        Recreating()
    elif iN == '3':
        ReadingWithFilter('wotdTDBY.txt')
        Recreating()
    elif iN == 'manualrun' or iN == 'ManualRun' or iN == 'Manualrun':
        print("Введите название txt файла(без .txt), находяшего в этой папке:")
        ReadingWithFilter(input()+'.txt')
        Recreating()
    elif iN == 'NewDayHorizon' or iN == 'Newdayhorizon' or iN == 'newdayhorizon':
        NewDayHorizon()
    elif iN == 'ManualSave' or iN == 'Manualsave' or iN == 'manualsave':
        print("Введите название откуда сохранить и куда(без .txt):")
        ReaderAndWriter(input('>')+'.txt', input('>')+'.txt')
    elif iN == 'AddNewWord' or iN == 'Addnewword' or iN == 'addnewword':
        print("Введите куда добавить(без .txt)!")
        Addition(input('>') + '.txt')
    else:
        print("Ошибка: Недопустимое значение!")

    if input('Продолжить...') == 'exit':
        print()
    else:
        Launch()

Launch()