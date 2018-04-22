from libs.models import *
from Domains.models import *

class Domains(object):
    def __init__(self, httpclient):
        self.httpclient = httpclient

    def ListDomains(self, perPage=0, page=1):
        """
        ListDomains returns all domains in the account. It omits some information that can be retrieved from GetDomain.
        Endpoint:   GET /v4/domains
        Parameters:
            perPage,	int32,	Per Page is the number of records to return per request. Per Page defaults to 1,000.
            page,	int32,	Page is which page to return
        """

        class Result(Model):
            domains = ListField(ModelField(Domain))

        if perPage != 0:
            headers = {"perPage": perPage, "page": page}
            response = self.httpclient.http_get("/v4/domains", headers)
        else:
            response = self.httpclient.http_get("/v4/domains")
        print response.__dict__

        if response.status != 200:
            raise NameHttpError(response)

        res = Result.from_json(response.body)
        return res.domains
