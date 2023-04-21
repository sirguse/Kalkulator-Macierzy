from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
import sys


#Tworzymy okno.
okno = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Kalkulator Macierzy")
window.setGeometry(500,400,500,400)

widget = QWidget()
layout = QGridLayout()

#Tworzymy przyciski
DodButton = QPushButton("Dodawanie")
OdeButton = QPushButton("Odejmowanie")
MnoButton = QPushButton("Mnozenie")
layout.addWidget(DodButton, 0, 0)
layout.addWidget(OdeButton, 0, 1)
layout.addWidget(MnoButton, 0, 2)

#Okno do wpisywania danych
Data = QWidget()
layoutData = QGridLayout()

#Pola do wpisywania danych
data1 = QLineEdit()
data2 = QLineEdit()
data3 = QLineEdit()
data4 = QLineEdit()
data5 = QLineEdit()
data6 = QLineEdit()
data7 = QLineEdit()
data8 = QLineEdit()
data9 = QLineEdit()

#Pola ukladu
layoutData.addWidget(data1, 0, 0)
layoutData.addWidget(data2, 0, 1)
layoutData.addWidget(data3, 1, 0)
layoutData.addWidget(data4, 1, 1)
layoutData.addWidget(data5, 2, 0)
layoutData.addWidget(data6, 2, 1)
layoutData.addWidget(data7, 3, 0)
layoutData.addWidget(data8, 3, 1)


#Przycisk do obliczania
ObliczButton = QPushButton('Oblicz')
layoutData.addWidget(ObliczButton, 4, 0, 1, 2)

#Etykieta do wyswietlania wynikow
label = QLabel()
layoutData.addWidget(label, 5, 0, 1, 2)










#Wyswietlamy okno
window.show()
sys.exit(okno.exec_())