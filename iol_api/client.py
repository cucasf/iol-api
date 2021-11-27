import aiohttp
import json
import logging
from datetime import date
from urllib.parse import urljoin

from iol_api.constants import *
from iol_api.utils import iol_decoder_hook, get_logger
from iol_api.token_manager import TokenManager


BASE_URL = 'https://api.invertironline.com/api/v2/'

class IOLClient:
    """
        Cliente para obtner datos de cuenta y mercado utilizando la API de Invertir Online
        https://api.invertironline.com
    """

    def __init__(self, username: str, password: str, logging_level=logging.NOTSET) -> None:
        self.logger = get_logger(__name__, logging_level)
        self.base_url = BASE_URL
        self.token_manager = TokenManager(username, password, logging_level=logging_level)
        
    async def _get_headers(self):
        header = {
            'Authorization': await self.token_manager.ensure_access_token()
        }
        return header

    async def _request(self, method, url, data_body=None, json_body=None) -> aiohttp.ClientResponse:
        url = urljoin(self.base_url, url)


        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=await self._get_headers(), data=data_body, json=json_body)as resp:
                
                if resp.status != 200 and resp.status != 202:
                    self.logger.warning(f'{resp.method} {resp.url} {resp.status}')
                else:
                    self.logger.info(f'{resp.method} {resp.url} {resp.status}')

                data = await resp.text()
        
        return json.loads(data, object_hook=iol_decoder_hook)
    
    #AsesoresTestInversor 
    async def get_asesores_test_inversor(self):
        path = 'asesores/test-inversor'
        return await self._request('GET', path)
    
    async def post_asesores_test_inversor(self, respuesta_inversor, id_cliente_asesorado=None):
        path = 'asesores/test-inversor'
        if id_cliente_asesorado:
            path = f'asesores/test-inversor/{id_cliente_asesorado}'
        return await self._request('GET', path, json_body=respuesta_inversor)
        
    # MiCuenta 
    async def get_estadocuenta(self):
        path = f'estadocuenta'
        return await self._request('GET', path)

    async def get_portafolio(self, pais):
        path = f'portafolio/{pais}'
        return await self._request('GET', path)

    async def get_operaciones(self, numero= None):
        path = 'operaciones'
        if numero:
            path = f'operaciones/{numero}'
        return await self._request('GET', path)
    
    async def delete_operaciones(self, numero):
        path = f'operaciones/{numero}'
        return await self._request('DELETE', path)

    # Operar
    async def post_operar_vender(self, orden_venta):
        path = 'operar/Vender'
        return await self._request('POST', path, json_body=orden_venta)

    async def post_operar_comprar(self, orden_compra):
        path = 'operar/Comprar'
        return await self._request('POST', path, json_body=orden_compra)

    async def post_operar_rescate_fci(self, orden_fci):
        path = 'operar/rescate/fci'
        return await self._request('POST', path, json_body=orden_fci)

    async def post_operar_suscripcion_fci(self, orden_fci):
        path = 'operar/suscripcion/fci'
        return await self._request('POST', path, json_body=orden_fci)

    # Titulos 
    async def get_fci(self, simbolo=None):
        path = 'titulos/fci'
        if simbolo:
            path = f'titulos/fci/{simbolo}'
        return await self._request('GET', path)
    
    async def get_fci_tipo_fondos(self):
        path = 'titulos/fci/tipofondos'
        return await self._request('GET', path)
    
    async def get_fci_administradoras(self):
        path = 'titulos/fci/administradoras'
        return await self._request('GET', path)
    
    async def get_fci_tipo_fondos_administradoras(self, administradora, tipo_fondo=None):
        path = f'titulos/fci/administradoras/{administradora}/tipofondos'
        if tipo_fondo:
            path = f'titulos/fci/administradoras/{administradora}/tipofondos/{tipo_fondo}'
        return await self._request('GET', path)

    async def get_instrumentos(self, pais):
        path= f'{pais}/titulos/cotizacion/instrumentos'
        return await self._request('GET', path)
    
    async def get_paneles(self, pais, instrumento):
        path= f'{pais}/titulos/cotizacion/paneles/{instrumento}'
        return await self._request('GET', path)

    async def get_titulo(self, simbolo, mercado):
        path = f'{mercado}/Titulos/{simbolo}'
        return await self._request('GET', path)
    
    async def get_titulo_opciones(self, simbolo, mercado):
        path = f'{mercado}/Titulos/{simbolo}/Opciones'
        return await self._request('GET', path)

    async def get_titulo_cotizacion(self, simbolo, mercado):
        path = f'{mercado}/Titulos/{simbolo}/Cotizacion'
        return await self._request('GET', path)

    async def get_titulo_historicos(self, simbolo, mercado, ajustada, fecha_desde:date=date(1970, 1, 1), fecha_hasta:date=date.today()):
        path = f'{mercado}/Titulos/{simbolo}/Cotizacion/seriehistorica/{fecha_desde.strftime("%Y-%m-%d")}/{fecha_hasta.strftime("%Y-%m-%d")}/{ajustada}'
        return await self._request('GET', path)

    async def get_panel_cotizaciones(self,  pais, instrumento, panel):
        path = f'Cotizaciones/{instrumento}/{panel}/{pais}'
        return await self._request('GET', path)

