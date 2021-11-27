=====
Usage
=====

To use IOL-API in a project::

    import asyncio
    from iol_api import IOLClient
    from iol_api.constants import Mercado

    async def main():

        iol_client = IOLClient('usurio@email.com', 'contrasena')

        simbolo = 'GGAL'

        t = await iol_client.get_titulo(simbolo, Mercado.BCBA)
        print(t)


    asyncio.run(main())

