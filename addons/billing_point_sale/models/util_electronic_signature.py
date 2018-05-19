# -*- coding: utf-8 -*-
from OpenSSL import crypto
import logging
module_logger = logging.getLogger('signature')
logger = logging.getLogger(__name__)


def read_signature(passwd, path):
    logger.info('become here')
    p12 = crypto.load_pkcs12(open("/path/to/cert.p12", 'rb').read(), 'Gagu2016')

    p12.get_certificate()     # (signed) certificate object
    p12.get_privatekey()      # private key.
    p12.get_ca_certificates()  # ca chain.


def expiration_date(file, password):
    pass


