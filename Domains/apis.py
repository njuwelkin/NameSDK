from libs.models import *
from Domains.models import *

class Domains(object):
    def __init__(self, httpclient):
        self.client = httpclient

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
            response = self.client.http_get("/v4/domains", headers)
        else:
            response = self.client.http_get("/v4/domains")
        print response.__dict__

        if response.status != 200:
            raise NameHttpError(response)

        try:
            res = Result.from_json(response.body)
        except Exception, description:
            raise NameParseError(description, response.body)

        return res.domains

    def GetDomain(self, domainName):
        """
        GetDomain returns details about a specific domain
        Endpoint:   GET /v4/domains/{domainName}
        Parameters:
        	domainName,	string,	DomainName is the domain to retrieve.
        """

        response = self.client.http_get("/v4/domains/%s" % domainName)

        if response.status != 200:
            raise NameHttpError(response)

        try:
            res = Domain.from_json(response.body)
        except Exception, description:
            raise NameParseError(description, response.body)

        return res

    def CreateDomain(self, body):
        """
        CreateDomain purchases a new domain. Domains that are not regularly priced require the purchase_price field to be specified.
        See https://www.name.com/api-docs/Domains#CreateDomain
        """
        class Result(Model):
            domain	= ModelField(Domain)
            order	= IntegerField()
            totalPaid	= FloatField()

        body._check_essential()
        





















