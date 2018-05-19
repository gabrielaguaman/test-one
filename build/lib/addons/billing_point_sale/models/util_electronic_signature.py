# -*- coding: utf-8 -*-
from OpenSSL import crypto


def read_signature(passwd):
    p12 = crypto.load_pkcs12(open("/path/to/cert.p12", 'rb').read(), passwd)

    p12.get_certificate()     # (signed) certificate object
    p12.get_privatekey()      # private key.
    p12.get_ca_certificates() # ca chain.

