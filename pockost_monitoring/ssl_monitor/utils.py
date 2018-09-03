import socket
import ssl
import OpenSSL


def get_certificat(domain):

    """Return a x509 certificat for given domain or domain:port

    :param domain: The domain or domain:port you want to retreive certificat
    :return: The x509 certificat
    """

    ctx = OpenSSL.SSL.Context(ssl.PROTOCOL_TLSv1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((domain, 443))
    cnx = OpenSSL.SSL.Connection(ctx, s)
    cnx.set_tlsext_host_name(domain)
    cnx.set_connect_state()
    cnx.do_handshake()

    return cnx.get_peer_certificate()
