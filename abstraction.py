class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua{temperatura}')

    def _agregar_jabon(self):
        print('Agregando jabon')\
    
    def _lavar(self):
        print('Lavando la ropa')

    def centrifugar(self):
        print('Centrifugando la ropa')

    