from namehttpclient import NameHTTPClient

class NameClient(NameHTTPClient):
    def __init__( self,
                  username,
                  token,
                  host      = NAMEDEBUGHOST,
                  port      = PORT,
                  timeout   = TIMEOUT,
                  force_tls = FORCE_TLS ):
        super(NameClient, self).__init__(username, token, host, port, timeout, force_tls)


