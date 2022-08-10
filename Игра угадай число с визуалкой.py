import random
import tkinter as tk
from random import randint, choice
from tkinter import messagebox

window = tk.Tk()

window.resizable(width= False, height= False)

window.title('Угодай число')

window.geometry('360x360')

window["bg"] = 'black'

def AddIdea():
    y = 1

    if y<6:
        i = int(EnterText.get())
        if i<n:
            tk.messagebox.showinfo('Результат', ('Загаданное число больше', 'Осталось', y, i, n, 'попыток'))
            y+=1
        elif True:
            tk.messagebox.showinfo('Результат', ('Загаданное число больше', 'Осталось', y, i, n, 'попыток'))
            y+=1





    # while y < 6:
    #     if n > i:
    #         print(y)
    #         print("Загаданное число больше")
    #         y += 1
    #     if n < i:
    #         print(y)
    #         print("Загаданное число меньше")
    #
    #         y += 1
    #
    #     if n == i:
    #         print("Число отгадано!")
    #         break
    #
    # if y == 6:
    #     print("Загаданное число:")
    #     print(n)



n = random.randint(1, 50)
#   загадываем число от 1 до 50
## 6 попыток пользователю,


EnterText = tk.Entry(fg = "black", width= "20")
EnterText.place(x = 120, y =70)




bth = tk.Button(window, text = 'Проверить', command= AddIdea, width = '13', height= '1', fg= "black", bg='white')
bth.place(x= 131, y= 110)

window.mainloop()