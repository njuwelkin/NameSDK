import base64
import httplib

NAMEHOST = "api.name.com"
NAMEDEBUGHOST = "api.dev.name.com"
PORT = 443
TIMEOUT = 10
FORCE_TLS = True

class NameResponse(object):
    def __init__(self, headers, status, reason, body):
        """ Constructor
        """
        self.headers = headers
        self.status  = status
        self.reason  = reason
        self.body    = body

    @classmethod
    def from_http_response(cls, http_response):
        return cls(
            headers = http_response.msg,
            status  = http_response.status,
            reason  = http_response.reason,
            body    = http_response.read())

    def getheader(self, header, default=None):
        """ Helper to match httplib.HttpResponse interface
        """
        return self.headers.get(header, default)

    def read(self, _ = None):
        """ Helper to match httplib.HttpResponse interface
        """
        return self.body


class NameHTTPClient(object):
    """Encapsulates the Name REST API.
    """
    def __init__( self,
                  username,
                  token,
                  host      = NAMEDEBUGHOST,
                  port      = PORT,
                  timeout   = TIMEOUT,
                  force_tls = FORCE_TLS ):
        """ Construct a new client object.
        """

        self.timeout   = timeout
        self.host      = host
        self.port      = port
        self.force_tls = force_tls
      

        self.basic_headers = {
            #'Accept'     : '*/*',
            }

        auth_token = 'Basic %s' % base64.standard_b64encode(
                '%s:%s' % ( username, token ))

        self.basic_headers['Authorization'] = auth_token

    def get_authorization(self):
        """ Returns the current authorization token for this Name
            client object, or None.
        """
        return self.basic_headers.get('Authorization', None)

    @staticmethod
    def _get_connection(host, port, force_tls):
        params = {"host": host, "port": port, "strict": True}

        #if timeout and sys.version_info >= (2, 6):
        #    params['timeout'] = timeout

        print(params)
        if force_tls:
            return httplib.HTTPSConnection(**params)
        else:
            return httplib.HTTPConnection(**params)
        

    @staticmethod
    def _raw_request(method,		# "GET"
                     uri,		# "/v4/hello"
                     headers,		# {'Authorization': 'Basic bmp...g=='}
                     body,
                     input_host,	# ""
                     input_port,
                     input_secure):
        """ Raw request handling function.  Takes a connection from the
            cache unless skip_cache is True.  Exceptions must be handled
            by the caller.
        """

        connection = NameHTTPClient._get_connection(
            host       = input_host,
            port       = input_port,
            force_tls  = input_secure)

        print("%s, %s, %s, %s" % (method, uri, body, headers))
        connection.request(
            method  = method,
            url     = uri,
            body    = body,
            headers = headers )

        response = NameResponse.from_http_response(
            connection.getresponse())

        return response

    def _request(self, method, uri, headers, body):
        assert(method.isupper())
        headers.update(self.basic_headers)
        return self._raw_request(method, uri, headers, body, self.host, self.port, self.force_tls)

    def _http_get(self, uri, headers, body):
        return self._request("GET", uri, headers, body)

    def _http_post(self, uri, headers, body):
        return self._request("POST", uri, headers, body)


class NameClient(NameHTTPClient):
    def __init__( self,
                  username,
                  token,
                  host      = NAMEDEBUGHOST,
                  port      = PORT,
                  timeout   = TIMEOUT,
                  force_tls = FORCE_TLS ):
        super(NameClient, self).__init__(username, token, host, port, timeout, force_tls)

    def __getattr__(self, name):
        return NameClient.UriElement(self, "/%s" % name)

    class UriElement(object):
        def __init__(self, client, path):
            self.client = client
            self.path = path

        def __getattr__(self, name):
            return NameClient.UriElement(self.client, "%s/%s" % (self.path, name))

        def get(self, headers={}, body=""):
            return self.client._http_get(self.path, headers, body)

        def post(self, headers={}, body=""):
            return self.client._http_post(self.path, headers, body)







