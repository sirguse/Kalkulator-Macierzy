import tkinter

# Tworzymy okno
okno = tkinter.Tk()
okno.title("Kalkulator macierzy 2x2")
okno.geometry('200x200')

# Tworzymy zmienne
a1 = tkinter.IntVar()
a2 = tkinter.IntVar()
b1 = tkinter.IntVar()
b2 = tkinter.IntVar()

# Tworzymy funkcje obliczające
def oblicz():
    a = int(a1.get())
    b = int(a2.get())
    c = int(b1.get())
    d = int(b2.get())
    wynik.configure(text="Wynik:" + str(a*d-b*c))
    

# Tworzymy przycisk oblicz
tkinter.Button(okno, text="Oblicz", command=oblicz).place(x=75,y=150)

# Tworzymy pola do wpisywania
tkinter.Label(okno, text='1.1').place(x=10, y=60)
tkinter.Entry(okno, textvariable=a1, width=5).place(x=30,y=60)

tkinter.Label(okno, text='1.2').place(x=70, y=60)
tkinter.Entry(okno, textvariable=a2, width=5).place(x=90,y=60)

tkinter.Label(okno, text='2.1').place(x=10, y=90)
tkinter.Entry(okno, textvariable=b1, width=5).place(x=30,y=90)

tkinter.Label(okno, text='2.2').place(x=70, y=90)
tkinter.Entry(okno, textvariable=b2, width=5).place(x=90,y=90)

# Tworzymy pole tekstowe na wynik
wynik = tkinter.Label(okno, text="Wynik:")
wynik.place(x=75,y=130)

# Uruchamiamy okno
okno.mainloop()