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

Ahora un ejemplo de como utilizar la libreria

.. code-block:: python

    import asyncio
    from iol_api import IOLClient
    from iol_api.constants import Mercado

    async def main():

        iol_client = IOLClient('usurio@email.com', 'contrasena')

        t = await iol_client.get_titulo('GGAL', Mercado.BCBA)
        
        print(t)

    asyncio.run(main())


**Descargo de responsabilidad:** *iol-api es una libreria no oficial. De ninguna manera esta
respaldada o asociada a INVERTIR ONLINE  o cualquier organización asociada.
Asegúrese de leer y comprender los términos de servicio de la API subyacente.
antes de usar este paquete. Estos autores no aceptan responsabilidad por
daños que pudieran derivarse del uso de este paquete. Consulte el archivo de LICENCIA para
más detalles.* 