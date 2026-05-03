from tkinter import ttk, StringVar
import tkinter as tk

#Cria a janela
janela = tk.Tk()
janela.title("Calculator")
janela.geometry("300x450")

#Ponte número para o display
num_equation = StringVar()

#Armazenamento do número
num_entry_value = ""

#Display da calculadora
display = tk.Entry(janela, width=50, font=("Arial", 35), textvariable=num_equation).place(x=0, y=0)

#Função Click -- para pegar o número e levar a informação para o num.equation e o num.entry_value
def click_num(num):
    global num_entry_value
    num_entry_value += str(num)
    num_equation.set(num_entry_value)

#Função Clear -- para limpar o display e o num.entry_value
def clear():
    global num_entry_value
    num_entry_value = ""
    num_equation.set(num_entry_value)

#Função Somar -- para somar os números do display
def somar():
    global num_entry_value
    try:
        num_entry_value = str(eval(num_entry_value))
        num_equation.set(num_entry_value)
    except:
        num_equation.set("Error")
        num_entry_value = ""

#Botões da calculadora -- command = dá o comando para o botão, nesse caso, a função click() que é responsável por pegar o número do botão e colocar no display
button1 = tk.Button(janela, text="(", width=11, height=3, command=lambda: click_num("(")).place(x=0, y=75)
button2 = tk.Button(janela, text=")", width=11, height=3, command=lambda: click_num(")")).place(x=75, y=75)
button3 = tk.Button(janela, text="%", width=11, height=3, command=lambda: click_num("%")).place(x=150, y=75)
button4 = tk.Button(janela, text="÷", width=11, height=3, command=lambda: click_num("/")).place(x=225, y=75)
button5 = tk.Button(janela, text="1", width=11, height=3, command=lambda: click_num("1")).place(x=0, y=150)
button6 = tk.Button(janela, text="2", width=11, height=3, command=lambda: click_num("2")).place(x=75, y=150)
button7 = tk.Button(janela, text="3", width=11, height=3, command=lambda: click_num("3")).place(x=150, y=150)
button8 = tk.Button(janela, text="x", width=11, height=3, command=lambda: click_num("*")).place(x=225, y=150)
button9 = tk.Button(janela, text="4", width=11, height=3, command=lambda: click_num("4")).place(x=0, y=225)
button10 = tk.Button(janela, text="5", width=11, height=3, command=lambda: click_num("5")).place(x=75, y=225)
button11 = tk.Button(janela, text="6", width=11, height=3, command=lambda: click_num("6")).place(x=150, y=225)
button12 = tk.Button(janela, text="-", width=11, height=3, command=lambda: click_num("-")).place(x=225, y=225)
button13 = tk.Button(janela, text="7", width=11, height=3, command=lambda: click_num("7")).place(x=0, y=300)
button14 = tk.Button(janela, text="8", width=11, height=3, command=lambda: click_num("8")).place(x=75, y=300)
button15 = tk.Button(janela, text="9", width=11, height=3, command=lambda: click_num("9")).place(x=150, y=300)
button16 = tk.Button(janela, text="+", width=11, height=3, command=lambda: click_num("+")).place(x=225, y=300)
button17 = tk.Button(janela, text="C", width=11, height=3, command=clear).place(x=0, y=375)
button18 = tk.Button(janela, text="0", width=11, height=3, command=lambda: click_num("0")).place(x=75, y=375)
button19 = tk.Button(janela, text=".", width=11, height=3, command=lambda: click_num(".")).place(x=150, y=375)
button20 = tk.Button(janela, text="=", width=11, height=3, command=somar).place(x=225, y=375)

#Deixa a janela ativa
janela.mainloop()
