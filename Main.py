import sys
from Persona import Persona
from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow,QLabel,QLineEdit, QVBoxLayout,QHBoxLayout,QApplication, QDialog, QWidget, QPushButton, QDialogButtonBox

personas = []

class AgregarDatos(QWidget):
    
    def __init__(self,identificador):
        super().__init__()
        self.identificador = identificador
        self.agregar()
        
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
        
        self.altura_input = QLineEdit(self)
        self.altura_input.resize(100,15)
        self.altura_input.move(100, 103)
        
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
        ventana.anadir(self.identificador, persona)
        self.hide()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio Taller Grupal")
        #Otras ventanas
        self.ventana_secundaria1 = AgregarDatos(1)
        self.ventana_secundaria2 = AgregarDatos(2)
        #Elementos
        boton_agregar1 = QPushButton("Agregar datos")
        boton_agregar2 = QPushButton("Agregar datos")
        boton_comparar = QPushButton("Comparar")
        #Connect
        boton_agregar1.clicked.connect(self.reaccion1)
        boton_agregar2.clicked.connect(self.reaccion2)
        #Labels
        bienvenida = QLabel("Bienvenido/a")
        instrucciones = QLabel("Aprete Agregar Datos para agregar los datos de cada persona (Altura y medida de Cintura en centimetros), luego aprete Comparar para comparar los ICA de las personas")
        self.nombre_objeto1 = QLabel("")
        self.cintura_objeto1 = QLabel("")
        self.altura_objeto1 = QLabel("")
        self.dato_objeto1 = QLabel("")
        self.nombre_objeto2 = QLabel("")
        self.cintura_objeto2 = QLabel("")
        self.altura_objeto2 = QLabel("")
        self.dato_objeto2 = QLabel("")
        self.comparador = QLabel("-")
        #Layouts
        contenedor_objeto1 = QVBoxLayout()
        contenedor_objeto1.addWidget(self.nombre_objeto1)
        contenedor_objeto1.addWidget(self.cintura_objeto1)
        contenedor_objeto1.addWidget(self.altura_objeto1)
        contenedor_objeto1.addWidget(self.dato_objeto1)
        contenedor_objeto1.addWidget(boton_agregar1)

        contenedor_objeto2 = QVBoxLayout()
        contenedor_objeto2.addWidget(self.nombre_objeto2)
        contenedor_objeto2.addWidget(self.cintura_objeto2)
        contenedor_objeto2.addWidget(self.altura_objeto2)
        contenedor_objeto2.addWidget(self.dato_objeto2)
        contenedor_objeto2.addWidget(boton_agregar2)

        contenedor_objetos_comparador = QHBoxLayout()
        contenedor_objetos_comparador.addLayout(contenedor_objeto1)
        contenedor_objetos_comparador.addWidget(self.comparador)
        contenedor_objetos_comparador.addLayout(contenedor_objeto2)

        contenedor_principal = QVBoxLayout()
        contenedor_principal.addWidget(bienvenida)
        contenedor_principal.addWidget(instrucciones)
        contenedor_principal.addLayout(contenedor_objetos_comparador)
        contenedor_principal.addWidget(boton_comparar)

        ventana_mayor = QWidget()
        ventana_mayor.setLayout(contenedor_principal)
        self.setCentralWidget(ventana_mayor)

    def reaccion1(self):
        if self.ventana_secundaria1.isHidden():
            self.ventana_secundaria1.show()
        else:
            self.ventana_secundaria1.hide()
    
    def reaccion2(self):
        if self.ventana_secundaria2.isHidden():
            self.ventana_secundaria2.show()
        else:
            self.ventana_secundaria2.hide()
            
    def anadir(self,identificador_ventana, objeto):
        if identificador_ventana == 1:
            personas.append(objeto)
            self.nombre_objeto1.setText(objeto.getNombre())
            self.cintura_objeto1.setText(f"{objeto.getCintura()}")
            self.altura_objeto1.setText(f"{objeto.getAltura()}")

        elif identificador_ventana == 2:
            personas.append(objeto)
            self.nombre_objeto2.setText(objeto.getNombre())
            self.cintura_objeto2.setText(f"{objeto.getCintura()}")
            self.altura_objeto2.setText(f"{objeto.getAltura()}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()

    ventana.show()
    app.exec()