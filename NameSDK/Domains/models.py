from NameSDK.libs.models import *

class Contact(Model):
    firstName		= StringField()
    lastName		= StringField()
    companyName		= StringField()
    address1		= StringField()
    address2		= StringField()
    city		= StringField()
    state		= StringField()
    zip			= StringField()
    country		= StringField()
    phone		= StringField()
    fax			= StringField()
    email		= StringField()

class Contacts(Model):
    registrant		= ModelField(Contact)
    admin		= ModelField(Contact)
    tech		= ModelField(Contact)
    billing		= ModelField(Contact)

class Domain(Model):
    domainName		= StringField()
    nameservers		= ListField(StringField())
    contacts		= ModelField(Contacts)
    privacyEnabled	= BoolField()
    locked		= BoolField()
    autorenewEnabled	= BoolField() 
    expireDate		= StringField()
    createDate		= StringField()
    renewalPrice	= FloatField()

############################ Post body ###############################
class DomainPurchase(Model):
    domain		= ModelField(Domain, notnull=True)
    purchasePrice	= FloatField(notnull=True)
    purchaseType	= StringField()
    years		= IntegerField()
    tldRequirements	= DictField()
    promoCode		= StringField()

class DomainRenew(Model):
    purchasePrice	= FloatField(notnull=True)
    years		= IntegerField()
    promoCode		= StringField()

class NameServers(Model):
    nameservers		= ListField(StringField())


############################ Response body ###########################
class DomainPurchaseResult(Model):
    domain      = ModelField(Domain)
    order       = IntegerField()
    totalPaid   = FloatField()


