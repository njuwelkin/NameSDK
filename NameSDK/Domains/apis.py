from NameSDK.libs.models import *
from NameSDK.libs.utils import *
from NameSDK.Domains.models import *

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
    def CreateDomain(self, body_DomainPurchase):
        """
        CreateDomain purchases a new domain. Domains that are not regularly priced require the purchase_price field to be specified.
        See https://www.name.com/api-docs/Domains#CreateDomain
        """
        body_DomainPurchase._check_essential()

        response = self.client.http_post("/v4/domains", body=json.dumps(body_DomainPurchase))
        return parse_response(response, DomainPurchaseResult)

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


    # not tested
    def RenewDomain(self, domainName, body_DomainRenew):
        """
        RenewDomain will renew a domain. Purchase_price is required if the renewal is not regularly priced.
        Endpoint:   POST /v4/domains/{domainName}:renew
        Parameters:
        	domainName,     string, DomainName is the domain name to disable autorenew for.
        	body,		DomainRenew
        		purchasePrice,	float64,	PurchasePrice is the amount to pay for the domain renewal. 
        						If VAT tax applies, it will also be added automatically. 
        						PurchasePrice is required if this is a premium domain.

        		years,		int32,		Years is for how many years to renew the domain for. 
        						Years defaults to 1 if not passed and cannot be more than 10.
        		promoCode,	string,		PromoCode is not yet implemented.
        """

        body._check_essential()
        response = self.client.http_post("/v4/domains/%s:renew" % domainName, json.dumps(body_DomainRenew))
        return parse_response(response, DomainPurchaseResult)

    def GetAuthCodeForDomain(self, domainName):
        """
        GetAuthCodeForDomain returns the Transfer Authorization Code for the domain.
        Endpoint:   GET /v4/domains/{domainName}:getAuthCode
        Parameters:
        	domainName,	string,	DomainName is the domain name to retrieve the authorization code for.
        """
        class Result(Model):
            authCode = StringField()
    
        response = self.client.http_get("/v4/domains/%s:getAuthCode" % domainName)
        return parse_response(response, Result).authCode

    # not implemented
    def PurchasePrivacy(self, domainName, body):
        pass


    # not tested
    def SetNameservers(self, domainName, body_NameServers):
        """
        SetNameservers will set the nameservers for the Domain.
        Endpoint:   POST /v4/domains/{domainName}:setNameservers
        Parameters:
        	domainName,	string,		DomainName is the domain name to disable autorenew for.
        	nameservers,	NameServers,	Namesevers is a list of the nameservers to set. 
        					Nameservers should already be set up and hosting the zone 
        					properly as some registries will verify before allowing the change.
        """
        body_NameServers._check_essential()
        response = self.client.http_post("/v4/domains/%s:setNameservers" % domainName, json.dumps(body_NameServers))
        return parse_response(response, Domain)

    def SetContacts(self, domainName, body_Contacts):
        body_Contacts._check_essential()
        response = self.client.http_post("/v4/domains/%s:setContacts" % domainName, json.dumps(body_Contacts))
        return parse_response(response, Domain)

    # not implemented
    #def LockDomain
    #def UnlockDomain
    #def CheckAvailability
    #def Search
    #def SearchStream


