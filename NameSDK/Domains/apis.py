from NameSDK.libs.models import *
from NameSDK.Domains.models import *
from NameSDK.libs.utils import *

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

        return parse_response(response, Result)


    def GetDomain(self, domainName):
        """
        GetDomain returns details about a specific domain
        Endpoint:   GET /v4/domains/{domainName}
        Parameters:
        	domainName,	string,	DomainName is the domain to retrieve.
        """

        response = self.client.http_get("/v4/domains/%s" % domainName)

        return parse_response(response, Domain)

    #
    # Not tested
    #
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

        response = self.client.http_post("/v4/domains", body=json.dumps(body))
        return parse_response(response, Result)

    # Not tested
    def EnableAutorenew(self, domainName):
        """
        EnableAutorenew enables the domain to be automatically renewed when it gets close to expiring.
        Endpoint:   POST /v4/domains/{domainName}:enableAutorenew
        Parameters:
        	domainName,	string,	DomainName is the domain name to enable autorenew for.
        """

        response = self.client.http_post("/v4/domains/%s:enableAutorenew" % domainName)
        return parse_response(response, Domain)

    def DisableAutorenew(self, domainName):
        """
        DisableAutorenew disables automatic renewals, thus requiring the domain to be renewed manually.
        Endpoint:   POST /v4/domains/{domainName}:disableAutorenew
        Parameters:
        	domainName,	string,	DomainName is the domain name to disable autorenew for.
        """

        response = self.client.http_post("/v4/domains/%s:disableAutorenew" % domainName)
        return parse_response(response, Domain)















