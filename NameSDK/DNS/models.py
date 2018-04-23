from NameSDK.libs.models import *
  
class DNSRecord(Model):
    """
    https://www.name.com/api-docs/types/record
    """
    id		= IntegerField()
    domainName	= StringField()
    host	= StringField()
    fqdn	= StringField()
    type	= StringField()
    answer	= StringField()
    ttl		= IntegerField()
    priority    = IntegerField()

############################ Post body ###############################
class ASDFPurchase(Model):
    #domain              = ModelField(Domain, notnull=True)
    #purchasePrice       = FloatField(notnull=True)
    #purchaseType        = StringField()
    #years               = IntegerField()
    tldRequirements     = DictField()
    promoCode           = StringField()



############################ Response body ###########################
    
