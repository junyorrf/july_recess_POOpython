class Escritor:
    def __init__(self, nome, ferramenta):
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, value):
        self.__ferramenta = value

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta está escrevendoo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendoo...')