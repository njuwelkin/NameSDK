from NameSDK.libs.models import *
from NameSDK.libs.utils import *
from NameSDK.DNS.models import *

class DNS(object):
    def __init__(self, httpclient):
        self.client = httpclient

    def ListRecords(self, domainName, perPage=0, page=0):
        """
        ListRecords returns all records for a zone.
        Endpoint:   GET /v4/domains/{domainName}/records
        Parameters:
        	domainName,	string,	DomainName is the zone to list the records for.
        	perPage,	int32,	Per Page is the number of records to return per request. Per Page defaults to 1,000.
        	page,		int32,	Page is which page to return.
        """

        class Result(Model):
            records	= ListField(ModelField(DNSRecord))
            nextPage	= IntegerField()
            lastPage	= IntegerField()

        if perPage != 0:
            headers = {"perPage": perPage, "page": page}
        else:
            headers = {}
        response = self.client.http_get("/v4/domains/%s/records" % domainName, headers)

        return parse_response(response, Result)

    def GetRecord(self, domainName, id):
        """
        GetRecord returns details about an individual record.
        Endpoint:   GET /v4/domains/{domainName}/records/{id}
        Parameters:
        	domainName,	string,	DomainName is the zone the record exists in
        	id,		int32,	ID is the server-assigned unique identifier for this record    
        """

        response = self.client.http_get("/v4/domains/%s/records/%s" % (domainName, id))
        return parse_response(response, DNSRecord)

    def CreateRecord(self, domainName, dnsRecord):
        """
        CreateRecord creates a new record in the zone.
        Endpoint:   POST /v4/domains/{domainName}/records
        Parameters:
        	dnsRecord,	DNSRecord,	see models for more info. id is ignored on create
        """
        response = self.client.http_post("/v4/domains/%s/records" % domainName, body=json.dumps(dnsRecord))

        return parse_response(response, DNSRecord)

    def UpdateRecord(self, domainName, id, dnsRecord):
        """
        UpdateRecord replaces the record with the new record that is passed.
        Endpoint:   PUT /v4/domains/{domainName}/records/{id}
        Parameters:
        	domainName,	string,		DomainName is the zone that the record belongs to.
        	id,		int32,		Unique record id. Value is ignored on Create, and must match the URI on Update.
        	dnsRecord,	DNSRecord,	see models for more info. id is ignored on update
        """
        response = self.client.http_put("/v4/domains/%s/records/%s" % (domainName, id), body=json.dumps(dnsRecord))

        return parse_response(response, DNSRecord)

    def DeleteRecord(self, domainName, id):
        """
        DeleteRecord deletes a record from the zone.
        Endpoint:   DELETE /v4/domains/{domainName}/records/{id}
        Parameters:
        	domainName,	string,	DomainName is the zone that the record to be deleted exists in.
        	id,		int32,	ID is the server-assigned unique identifier for the Record to be deleted. 
        				If the Record with that ID does not exist in the specified Domain, an error is returned.
        """
        response = self.client.http_delete("/v4/domains/%s/records/%s" % (domainName, id))
        parse_response(response, None)















