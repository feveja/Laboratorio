class Persona:
    def __init__(self, nombre, cintura, altura):
        self.__nombre = nombre
        self.__cintura = int(cintura)
        self.__altura = int(altura)
    
    def getNombre(self):
        return self.__nombre
    def getCintura(self):
        return self.__cintura
    def getAltura(self):
        return self.__altura
    def getICA(self):
        return self.__cintura/self.__alturas