=======
iol-api libreria para consumir Invertir Online API en Python
=======

.. image:: https://img.shields.io/pypi/v/iol_api.svg
        :target: https://pypi.python.org/pypi/iol_api

Que es iol-api
--------------

iol-api es una libreria no oficial para consumir datos de `Inververtir Online API <https://api.invertironline.com>`_

La libreria esta diseñana para funcinar asincronicamente utilizando aiohttp.


Como usarlo
-----------

Es necesiro contar con una cuenta en Invertir Online y tener activado el uso de la API.

Luego, instalar iol-api

.. code-block:: python

    pip install iol-api

Ejemplo de como utilizar la libreria

.. code-block:: python

    import asyncio
    from iol_api import IOLClient
    from iol_api.constants import Mercado

    async def main():

        iol_client = IOLClient('usurio@email.com', 'contrasena')

        data = await iol_client.get_titulo('SUPV', Mercado.BCBA)
        
        print(data)

    asyncio.run(main())

iol-api devulve un diccionario con objetos nativos de Python, transformado cualquier fecha en un objecto de clase datetime

Funciones Disponibles 
---------------------

Informacion de mercardo

.. code-block:: python
    
    data = await iol_client.get_instrumentos(Pais.ARG)
    
.. code-block:: python
    
    data = await iol_client.get_paneles(Pais.ARG, Instrumento.ARG)

.. code-block:: python
    
    data = await iol_client.get_panel_cotizaciones(Pais.ARG, Instrumento.ARG, Panel.ARG.ACCIONES.MERVAL)

.. code-block:: python
    
    data = await iol_client.get_titulo('SUPV', Mercado.BCBA)
    
.. code-block:: python
    
    data = await iol_client.get_titulo_opciones('SUPV', Mercado.BCBA)
    
.. code-block:: python
    
    data = await iol_client.get_titulo_cotizacion('SUPV', Mercado.BCBA)
    
Para obtener historios es neceserio crear 2 objetos date para definir fecha_desde y fecha_hasta

.. code-block:: python
    
    data = await iol_client.get_titulo_historicos('SUPV', Mercado.BCBA, Ajustada.AJUSTADA, fecha_desde=date(2021,1,1), fecha_hasta=date.today())

.. code-block:: python
    
    data = await iol_client.get_fci()

.. code-block:: python
    
    data = await iol_client.get_fci('PRPLPEB')

.. code-block:: python
    
    data = await iol_client.get_fci_administradoras()

.. code-block:: python
    
    data = await iol_client.get_fci_tipo_fondos_administradoras(Administradora.SUPERVIELLE)

.. code-block:: python
    
    data = await iol_client.get_fci_tipo_fondos_administradoras(Administradora.SUPERVIELLE, TipoFondo.RENTA_FIJA_PESOS)
  
Operar 

.. code-block:: python

    ord_compra = {
            "mercado": Mercado.BCBA,
            "simbolo": 'SUPV', 
            "tipoOrden": TipoDeOrden.PRECIO_LIMITE,
            "cantidad": 1,
            "precio": 50,
            "plazo": Plazo.T2,
            "validez": '2021-12-01T17:00:00.000Z'
        }
    
    data_ord = await iol_client.post_operar_comprar(ord_compra)

.. code-block:: python

    data_del =  await iol_client.delete_operaciones(data_ord['numeroOperacion'])

.. code-block:: python

    ord_venta = {
            "mercado": Mercado.BCBA,
            "simbolo": 'SUPV', 
            "tipoOrden": TipoDeOrden.PRECIO_LIMITE,
            "cantidad": 1,
            "precio": 150,
            "plazo": Plazo.T2,
            "validez": '2021-12-01T17:00:00.000Z'
        }
    
    data_ord = await iol_client.post_operar_vender(ord_venta)

.. code-block:: python

    ord_fci = {
            "simbolo": 'PRPLPEB',
            "cantidad": 100,
            "soloValidar": True
        }

    resp_ord = await iol_client.post_operar_suscripcion_fci(ord_fci)

.. code-block:: python

    resp_ord = await iol_client.post_operar_rescate_fci(ord_fci)

iol-api cuenta con clases para facilitar la creacion de ordenes de compras, ventas y fci.

* OrdenCompra 
* OrdenVenta
* OrdenFCI

.. code-block:: python

    from iol_api import IOLClient, OrdenCompra, OrdenVenta, OrdenFCI


    ord_compra = OrdenCompra(
        Mercado.BCBA,
        'SUPV',
        cantidad=1,
        precio=50,
        tipo_orden=TipoDeOrden.PRECIO_LIMITE,
        plazo=Plazo.T2,
        validez=datetime(2021, 12, 1)
    )
    
    data_ord = await iol_client.post_operar_comprar(ord_compra.crear())

Estado de cuenta y operaciones

.. code-block:: python

    data = await iol_client.get_estadocuenta()

.. code-block:: python

    data = await iol_client.get_portafolio(Pais.ARG)

.. code-block:: python

    data = await iol_client.get_operaciones()

.. code-block:: python

    data = await iol_client.get_operaciones(12345678)
    
**Descargo de responsabilidad:** *iol-api es una libreria no oficial. De ninguna manera esta
respaldada o asociada a INVERTIR ONLINE  o cualquier organización asociada.
Asegúrese de leer y comprender los términos de servicio de la API subyacente.
antes de usar este paquete. Estos autores no aceptan responsabilidad por
daños que pudieran derivarse del uso de este paquete. Consulte el archivo de LICENCIA para
más detalles.* 