# -*- coding: utf-8 -*-

import requests

MSG_SCHEMA_INVALID = u"El sistema generó correctamente el XML, pero  el comprobante electrónico no pasa la validación" \
                     u" del SRI."

API_TEST_RECEIV = 'https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantes?wsdl'  # noqa
API_TEST_AUTH = 'https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantes?wsdl'  # noqa
API_RECEIV = 'https://cel.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantes?wsdl'  # noqa
API_AUTH = 'https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantes?wsdl'  # noqa


# Ambiente de Pruebas:
URL_TEST_RECEIVE = 'https://celcer.sri.gob.ec/comprobantes-electronicosws/RecepcionComprobantesOffline?wsdl'
URL_TEST_AUTH = 'https://celcer.sri.gob.ec/comprobantes-electronicosws/AutorizacionComprobantesOffline?wsdl'

# Ambiente de Producción:
URL_PRODUCTION_RECEIVE = 'https://cel.sri.gob.ec/comprobantes-electronicosws/RecepcionComprobantesOffline?wsdl'
URL_PRODUCTION_AUTH = 'https://cel.sri.gob.ec/comprobantes-electronicosws/AutorizacionComprobantesOffline?wsdl'


def check_service(env='prueba'):
    flag = False
    if env == 'prueba':
        URL = URL_TEST_RECEIVE
    else:
        URL = URL_PRODUCTION_RECEIVE

    for i in [1, 2, 3]:
        try:
            res = requests.head(URL, timeout=3)
            flag = True

        except requests.exceptions.RequestException:
            return flag, False
    return flag, res


