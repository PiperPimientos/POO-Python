class Automovil:

    # def __init__(self, modelo, marca, color):
    #     self.modelo = modelo
    #     self.marca = marca
    #     self.color = color
    #     self._estado = 'en reposo'
    #     self._motor = None

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    #Metodo para la aceleracion del Automovil
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor_inyecta_gasolina(10)
        else:
            self._motor._inyecta_gasolina(3)    

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass