from datetime import datetime
from pagina import Cotizador
from tkinter import ttk
from tkinter import *

class Aplicacion():
    __ventana = None
    __compras = []
    __ventas = []
    __fecha = None
    __cotizador = None
    __labels_compra = []
    __labels_venta = []

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Cotizaciones del dolar')
        self.__ventana.resizable(0, 0)

        self.__cotizador = Cotizador()
        self.__cotizador.conectar()
        self.__fecha = StringVar()
        self.__labels_compra = []
        self.__compras = []
        self.__ventas = []
        self.__labels_venta = []

        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief='groove', padding=(10,10)).grid(column=0, row=0)
        self.label1 = ttk.Label(self.marco, text='Moneda').grid(column=0, row=0, columnspan=2, padx=(0, 150), sticky=E)
        self.label2 = ttk.Label(self.marco, text='Compra').grid(column=2, row=0, sticky=W)
        self.label3 = ttk.Label(self.marco, text='Venta').grid(column=3, row=0, sticky=W)
        self.separador1 = ttk.Separator(self.marco, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky=(W, E))
        i = 0
        for tipo in self.__cotizador._tipos():
            compra = StringVar()
            venta = StringVar()
            self.__compras.append(compra)
            self.__ventas.append(venta)
            self.tipo = ttk.Label(self.marco, text=tipo).grid(column=0, row=i + 2, columnspan=2, padx=(0, 150), pady=(10, 0), sticky=W)
            lbl_compra = ttk.Label(self.marco, textvariable=self.__compras[i]).grid(column=2, row=i + 2, pady=(10, 0), sticky=W)
            lbl_venta = ttk.Label(self.marco, textvariable=self.__ventas[i]).grid(column=3, row=i + 2, pady=(10, 0), sticky=W)
            self.__labels_compra.append(lbl_compra)
            self.__labels_venta.append(lbl_venta)
            i += 1
        self.separador2 = ttk.Separator(self.marco).grid(column=0, row=i + 3, columnspan=4, pady=(10, 0), sticky=(W, E))
        self.botonactualizar = ttk.Button(self.marco, text="Actualizar", command=self.actualizar).grid(column=0, row=i + 4, padx=(0, 100), sticky=W)
        self.lbl_fecha = ttk.Label(self.marco, textvariable=self.__fecha).grid(column=1, row=i + 4, columnspan=3,sticky=W)
        self.actualizar()
        self.__ventana.mainloop()

    def actualizar(self):
        self.__cotizador.conectar()
        i = 0
        for tipo in self.__cotizador._tipos():
            compra = self.__cotizador.preciocompra(tipo)
            venta = self.__cotizador.precioventa(tipo)
            self.__compras[i].set(compra)
            self.__ventas[i].set(venta)
            i += 1
        fecha = datetime.today()
        fecha = fecha.strftime('%d/%m/%Y, %H:%M:%S')
        self.__fecha.set('Actualizado ' + fecha)

if __name__ == '__main__':
    miapp = Aplicacion()