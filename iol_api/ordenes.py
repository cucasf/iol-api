from datetime import datetime

from iol_api.constants import Plazo, TipoDeOrden

class OrdenCompra:
    """
         ComprarBindingModel {
            mercado (string): = ['bCBA', 'nYSE', 'nASDAQ', 'aMEX', 'bCS', 'rOFX'],
            simbolo (string): ,
            cantidad (number, optional): ,
            precio (number): ,
            validez (string): ,
            tipoOrden (string, optional) = ['precioLimite', 'precioMercado'],
            plazo (string): = ['t0', 't1', 't2'],
            monto (number, optional)
        } 
    """
    def __init__(self, mercado, simbolo,  validez=None, cantidad=None, monto=None, precio=0, tipo_orden=TipoDeOrden.PRECIO_LIMITE, plazo=Plazo.T2) -> None:
        self.type = type
        self.mercado = mercado
        self.simbolo = simbolo
        self.cantidad = cantidad
        self.precio = precio

        if validez is not None:
            self.validez = validez
        else:
            self.set_validez()

        self.tipo_orden = tipo_orden
        self.plazo = plazo
        self.monto = monto
        self._validar()

    def _validar(self):
        if self.monto is not None and self.cantidad is not None:
            raise AttributeError("Parametro monto y cantidad definidos, solo se puede usar uno de los dos parametros por orden")

        if self.cantidad is not None and self.tipo_orden != TipoDeOrden.PRECIO_LIMITE:
            raise AttributeError("cantidad solo permite tipo_orden='precioLimite'")

        if self.tipo_orden == TipoDeOrden.PRECIO_MERCADO and self.precio > 0:
            raise AttributeError("Precio debe ser 0 para tipo_orden='precioMercado'")

        if self.tipo_orden == TipoDeOrden.PRECIO_LIMITE and self.precio <= 0:
            raise AttributeError("Precio debe ser mayor que 0 para tipo_orden='precioLimite'")

    def set_validez(self):
        dt = datetime.now()
        self.validez = datetime(dt.year, dt.month, dt.day, 23, 59, 59)
        
    def crear(self):
        ord = {
            "mercado": self.mercado,
            "simbolo": self.simbolo,
            "tipoOrden": self.tipo_orden,
            "precio": self.precio,
            "plazo": self.plazo,
            "validez": self.validez.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        }

        if self.cantidad is not None:
            ord["cantidad"] = self.cantidad
        else:
            ord["monto"] = self.monto
        
        return ord

class OrdenVenta:
    """
        VenderBindingModel {
            mercado (string): = ['bCBA', 'nYSE', 'nASDAQ', 'aMEX', 'bCS', 'rOFX'],
            simbolo (string): ,
            cantidad (number): ,
            precio (number): ,
            validez (string): ,
            tipoOrden (string, optional) = ['precioLimite', 'precioMercado'],
            plazo (string, optional) = ['t0', 't1', 't2']
        } 
    """

    def __init__(self, mercado, simbolo, cantidad, validez=None, precio=0, tipo_orden=TipoDeOrden.PRECIO_LIMITE, plazo=Plazo.T2) -> None:
        self.type = type
        self.mercado = mercado
        self.simbolo = simbolo
        self.cantidad = cantidad
        self.precio = precio

        if validez:
            self.validez = validez
        else:
            self.set_validez()

        self.tipo_orden = tipo_orden
        self.plazo = plazo
        self._validar()

    def _validar(self):
        if self.cantidad is not None:
            raise AttributeError("Parametro cantidad no definido")

        if self.tipo_orden == TipoDeOrden.PRECIO_MERCADO and self.precio > 0:
            raise AttributeError("Precio debe ser 0 para tipo_orden='precioMercado'")

        if self.tipo_orden == TipoDeOrden.PRECIO_LIMITE and self.precio <= 0:
            raise AttributeError("Precio debe ser mayor que 0 para tipo_orden='precioLimite'") 

    def set_validez(self):
        dt = datetime.now()
        self.validez = datetime(dt.year, dt.month, dt.day, 23, 59, 59)
        
    def crear(self):
        ord = {
            "mercado": self.mercado,
            "simbolo": self.simbolo,
            "tipoOrden": self.tipo_orden,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "plazo": self.plazo,
            "validez": self.validez.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        }
        return ord

class OrdenFCI:

    def __init__(self, simbolo, cantidad, solo_validar) -> None:
        self.simbolo = simbolo 
        self.cantidad = cantidad 
        self.solo_validar = solo_validar 

    def crear(self):
        ord = {
            "simbolo": self.simbolo,
            "cantidad": self.cantidad,
            "soloValidar": self.solo_validar
        }
        return ord