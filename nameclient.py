from namehttpclient import NameHTTPClient

import settings

NAMEHOST = "api.name.com"
NAMEDEBUGHOST = "api.dev.name.com"
PORT = 443
TIMEOUT = 10
FORCE_TLS = True


#
# use meta class here is only for update the __doc__. 
# not related to any functionality
#
class ClientMeta(type):
    def __new__(cls, name, bases, attrs):
        assert(name=='NameClient')

        doc = "Supported modules: "
        for k in settings.modules.keys():
            doc += "\"%s\", " % k
        doc += "use help(%s_instance.{modules}) for details." % name
        attrs["__doc__"] = doc
        return super(ClientMeta,cls).__new__(cls, name, bases, attrs)


class NameClient(object):
    __metaclass__ = ClientMeta

    def __init__( self,
                  username,
                  token,
                  host      = NAMEDEBUGHOST,
                  port      = PORT,
                  timeout   = TIMEOUT,
                  force_tls = FORCE_TLS ):
        
        self.http_client = NameHTTPClient(username, token, host, port, timeout, force_tls)
        for k, v in settings.modules.iteritems():
            self.__dict__[k] = v(self.http_client)



