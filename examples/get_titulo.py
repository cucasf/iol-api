import asyncio
from iol_api import IOLClient
from iol_api.constants import Mercado

async def main():

    iol_client = IOLClient('usurio@email.com', 'contrasena')

    t = await iol_client.get_titulo('GGAL', Mercado.BCBA)
    
    print(t)


asyncio.run(main())