import requests


class Cotizador:
    __url = None
    __cargar = None
    __cotizacion = None

    def __init__(self):
        self.__url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        self.__cargar =  None
        self.__cotizaciones = None

    def conectar(self):
        self.__cargar = requests.get(self.__url)
        self.__cotizaciones = self.__cargar.json()

    def _tipos(self):
        _tipos = []
        for tipo in self.__cotizaciones:
            nombre = tipo['casa']['nombre'].lower()
            if nombre.find('dolar') != -1:
                _tipos.append(nombre)
        return _tipos

    def precioventa(self, nombre):
        i = 0
        esta = False
        while i < len(self.__cotizaciones) and not esta:
            nomcoti = self.__cotizaciones[i]['casa']['nombre']
            if nomcoti.lower() == nombre.lower():
                esta = True
            else:
                i += 1
        cotizacion = self.__cotizaciones[i]['casa']['venta']
        if cotizacion.lower() != 'no cotiza':
            cotizacion = cotizacion.replace(',', '.')
            cotizacion = float(cotizacion)
        return cotizacion

    def preciocompra(self, nombre):
        i = 0
        esta = False
        while i < len(self.__cotizaciones) and not esta:
            nomcoti = self.__cotizaciones[i]['casa']['nombre']
            if nomcoti.lower() == nombre.lower():
                esta = True
            else:
                i += 1
        cotizacion = self.__cotizaciones[i]['casa']['compra']
        if cotizacion.lower() != 'no cotiza':
            cotizacion = cotizacion.replace(',', '.')
            cotizacion = float(cotizacion)
        return cotizacion
