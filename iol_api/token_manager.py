import asyncio
from datetime import timedelta, datetime
import json

import aiohttp
import logging

from typing import Any

from iol_api.constants import *
from iol_api.utils import get_logger, iol_decoder_hook

TOKEN_ENDPOINT = 'https://api.invertironline.com/token'
DEFAULT_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

class TokenManager:

    def __init__(self, username, password, logging_level=logging.NOTSET) -> None:
        self.logger = get_logger(__name__, logging_level)
        self._username = username
        self._password = password
        self.token = None
        self.sem = asyncio.Semaphore(1)
    
    async def ensure_access_token(self):

        while self.sem.locked():
            await asyncio.sleep(1)
        
        async with self.sem:
            datetime_now = datetime.utcnow() + timedelta(seconds=60)

            if self.token is None or self.token['.refreshexpires'] < datetime_now:
                await self._get_token()
            elif self.token['.expires'] < datetime_now:
                await self._refresh_token()

            return f"{self.token['token_type'].title()} {self.token['access_token']}"

    async def _fetch_token(self, data) -> Any:

        async with aiohttp.ClientSession() as session:
            async with session.post(TOKEN_ENDPOINT, headers=DEFAULT_HEADERS, data=data) as resp:
                if resp.status != 200:
                    raise ConnectionError(f'Authentication Error {resp.status} {resp.headers}')

                self.token = json.loads(await resp.text(), object_hook=iol_decoder_hook)

                self.logger.info(f"Succes authentication. Token expires: {self.token['.expires']}, refreshexpires: {self.token['.refreshexpires']}")
                return self.token
    
    async def _get_token(self) -> Any:
        self.logger.debug("Getting Token")
        data = {
            "username": self._username,
            "password": self._password,
            "grant_type": "password"
        }
        return await self._fetch_token(data)

    async def _refresh_token(self) -> Any:
        self.logger.debug("Refreshing Token")
        data = {
            "refresh_token": self.token['refresh_token'],
            "grant_type": "refresh_token"
        }
        return self._fetch_token(data)

