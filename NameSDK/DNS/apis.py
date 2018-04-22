from NameSDK.libs.models import *
from NameSDK.libs.utils import *
from NameSDK.DNS.models import *

class DNS(object):
    def __init__(self, httpclient):
        self.client = httpclient
