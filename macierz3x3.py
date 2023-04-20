
'''
okno = tk.Tk()
okno.title("3x3")
okno.geometry('300x300')

def oblicz():
    a = int(a11.get())
    b = int(a12.get())
    c = int(a13.get())
    
    d = int(b21.get())
    e = int(b22.get())
    f = int(b23.get())
    
    g = int(c31.get())
    h = int(c32.get())
    i = int(c33.get())


#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a new function to open the window
def open_win():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)
#Create a label
Label(win, text= "Click the below button to Open a New Window", font= ('Helvetica 17 bold')).pack(pady=30)
#Create a button to open a New Window
ttk.Button(win, text="Open", command=open_win).pack()
win.mainloop()
'''

import tkinter as tk
from tkinter import messagebox

okno = tk.Tk()
okno.title('Macierze')
okno.geometry('400x400')





def Dodawanie():
    new = tk.Tk()
    new.geometry('500x200')
    new.title('Dodawanie')
    tk.Label(new, text="Dodawanie macierzy 3x3").place(x=150,y=150)
    
    tk.Label(new, text='1.1').place(x=10, y=60)
    tk.Entry(new, textvariable=a11, width=5).place(x=30,y=60)
    
    tk.Label(new, text='1.2').place(x=70, y=60)
    tk.Entry(new, textvariable=a12, width=5).place(x=90,y=60)
    
    tk.Label(new, text='1.3').place(x=130, y=60)
    tk.Entry(new, textvariable=a13, width=5).place(x=150,y=60)

    tk.Label(new, text='2.1').place(x=70, y=90)
    tk.Entry(new, textvariable=a13, width=5).place(x=30,y=90)

    tk.Label(new, text='2.2').place(x=70, y=90)
    tk.Entry(new, textvariable=b21, width=5).place(x=90,y=90)
    

    
    tk.Button(new, text="Oblicz", command=obliczdod).place(x=75,y=150)
wynik = tk.Label(okno, text="Wynik:")
wynik.place(x=75,y=130)
    


    
    
    
def Odejmowanie():
    new1 = tk.Tk()
    new1.geometry('300x300')
    new1.title('Odejmowanie')
    tk.Label(new1, text="Odejmowanie macierzy 3x3").place(x=150,y=150)
def Mnozenie():
    new2 = tk.Tk()
    new2.geometry('300x300')
    new2.title('Mnozenie')
    tk.Label(new2, text="Mnozenie macierzy 3x3").place(x=150,y=150)
  
  
  
    
tk.Label(okno, text="Wybierz dzialanie").pack(pady=30)

tk.Button(okno, text="Dodawanie",command=Dodawanie).pack()
tk.Button(okno, text="Odejmowanie",command=Odejmowanie).pack()
tk.Button(okno, text="Mnozenie",command=Mnozenie).pack()
 
 
a11 = tk.IntVar()
a12 = tk.IntVar()
a13 = tk.IntVar()

b21 = tk.IntVar()
b22 = tk.IntVar()
b23 = tk.IntVar()

c31 = tk.IntVar()
c32 = tk.IntVar()
c33 = tk.IntVar()

a111 = tk.IntVar()
a122 = tk.IntVar()
a133 = tk.IntVar()

b211 = tk.IntVar()
b222 = tk.IntVar()
b233 = tk.IntVar()

c311 = tk.IntVar()
c322 = tk.IntVar()
c333 = tk.IntVar()

def obliczdod():
    a = int(a11.get()) #1.1
    b = int(a12.get()) #1.2
    c = int(a13.get()) #1.3
    
    d = int(b21.get()) #2.1
    e = int(b22.get()) #2.2
    f = int(b23.get()) #2.3
    
    g = int(c31.get()) #3.1
    h = int(c32.get()) #3.2
    i = int(c33.get()) #3.3
    
    a_1 = int(a111.get()) #1.1
    b_1 = int(a122.get()) #1.2
    c_1 = int(a133.get()) #1.3
    
    d_1 = int(b211.get()) #2.1
    e_1 = int(b222.get()) #2.2
    f_1 = int(b233.get()) #2.3
    
    g_1 = int(c311.get()) #3.1
    h_1 = int(c322.get()) #3.2
    i_1 = int(c333.get()) #3.3
    
    wynik_1= (a+a_1)
    wynik_2 = (b+b_1)
    wynik_3 = (c+c_1)
    
    wynik_4 = (d+d_1)
    wynik_5 = (e+e_1)
    wynik_6 = (f+f_1)
    
    wynik_7 = (g+g_1)
    wynik_8 = (h+h_1)
    wynik_9 = (i+i_1)
    wynik.configure(text=wynik_1)
    


    



    


    







okno.mainloop()

    
    
