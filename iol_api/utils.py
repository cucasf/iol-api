import re
import pandas as pd
from datetime import datetime

import logging
import sys

def iol_decoder_hook(dct):
    for k, v in dct.items():
        if (isinstance(v, str)):
            #2021-11-24T17:00:22.082Z
            if re.match('(\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\.\d{3}Z)',v):

                dct[k] = datetime.utcfromtimestamp(pd.to_datetime(v, format='%Y-%m-%dT%H:%M:%S.%fZ').timestamp())

            #2021-11-24T16:04:25.2370547-03:00
            elif re.match('(\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}\.\d{7}[+-]\d{2}\:\d{2})',v):
                dct[k] = datetime.utcfromtimestamp(pd.to_datetime(v, format='%Y-%m-%dT%H:%M:%S.%f%z').timestamp())
            
            #Fri, 26 Nov 2021 18:15:14 GMT
            elif re.match('([a-zA-Z]{3}, \d{2} [a-zA-Z]{3} \d{4} \d{2}\:\d{2}\:\d{2} [A-Z]{3})',v):
                dct[k] = datetime.utcfromtimestamp(pd.to_datetime(v, format='%a, %d %b %Y %H:%M:%S %Z').timestamp())

            #0001-01-01T00:00:00
            elif re.match('(\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2})',v):
                dct[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')

    return dct


def get_logger(name, level):

    formatter = logging.Formatter("%(levelname)s:%(name)s: %(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger