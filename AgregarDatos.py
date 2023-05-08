import sys
from Persona import Persona
from PyQt6.QtWidgets  import QWidget, QLabel, QPushButton, QLineEdit, QApplication
from PyQt6.QtGui import QFont

class AgregarDatos(QWidget):
    
    def __init__(self):
        super().__init__()
        self.agregar()
        self.show()
        
    def agregar(self):
        self.setGeometry(100,100,300,200)
        self.setWindowTitle("Ingreso Datos de Persona")
        
        ingreso_label =QLabel(self)
        ingreso_label.setText("Ingreso de Datos")
        ingreso_label.setFont(QFont("",15))
        ingreso_label.move(25,25)
        
        nombre_label = QLabel(self)
        nombre_label.setText("Nombre:")
        nombre_label.setFont(QFont("",10))
        nombre_label.move(30, 63)
        
        self.nombre_input = QLineEdit(self)
        self.nombre_input.resize(100,15)
        self.nombre_input.move(100, 63)
        
        cintura_label = QLabel(self)
        cintura_label.setText("Cintura:")
        cintura_label.setFont(QFont("",10))
        cintura_label.move(30,83)
        
        self.cintura_input = QLineEdit(self)
        self.cintura_input.resize(100,15)
        self.cintura_input.move(100, 83)
        
        altura_label = QLabel(self)
        altura_label.setText("Altura:")
        altura_label.setFont(QFont("",10))
        altura_label.move(30, 103)
        
        self.altura_label = QLineEdit(self)
        self.altura_label.resize(100,15)
        self.altura_label.move(100, 103)
        
        boton = QPushButton(self)
        boton.setText("Agregar")
        boton.resize(150, 30)
        boton.move(60, 130)
        boton.clicked.connect(self.crearPersona)
    
    def crearPersona(self):
        nombre = self.nombre_input.text()
        cintura = self.cintura_input.text()
        altura = self.altura_input.text()
        persona = Persona(nombre, cintura, altura)