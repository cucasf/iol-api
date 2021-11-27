import asyncio

from iol_api import IOLClient
from iol_api.constants import Mercado

def do_something(data):
    print(data) 

async def inf_loop(iol_client, simbolo, mercado, call=None, timesleep=10):

    while True:
        resp = await iol_client.get_titulo(simbolo, mercado)
        call(resp)
        await asyncio.sleep(timesleep)

async def main():

    iol_client = IOLClient('usurio@email.com', 'contrasena')
    
    t1 = inf_loop(iol_client, 'ALUA', Mercado.BCBA, do_something)
    t2 = inf_loop(iol_client, 'GGAL', Mercado.BCBA, do_something)

    loop = asyncio.get_event_loop()
    print('Creating task t1')
    loop.create_task(t1)
    print('Creating task t2')
    loop.create_task(t2)
    print('All task created')

    await asyncio.sleep(15)

    print('I can do more things')

loop = asyncio.get_event_loop()
try:
    loop.create_task(main())
    loop.run_forever()
except:
    loop.stop()
    loop.close()
