from NameSDK.nameerror import *
from NameSDK.nameclient import *

try:

	#print NameClient.__doc__
	#print help(NameClient)

	n=NameClient(username="username", token="ad1.......", host=NAMEHOST)

	print "################## ListDomains #################"
	print n.Domains.ListDomains()


	print "################## GetDomain #################"
	domain = n.Domains.GetDomain("facebook.com")
	print domain

	#print "################## EnableAutorenew #################"
	#domain = n.Domains.EnableAutorenew("facebook.com")
	#print domain.autorenewEnabled

	#print "################## DisableAutorenew #################"
	#domain = n.Domains.DisableAutorenew("facebook.com")
	#print domain
	#print domain.autorenewEnabled

	#print "################## Renew #################"
	#purchase = n.Domains.RenewDomain("facebook.com", DomainRenew(purchasePrice=1, years=1))
        #print purchase

	#print "################## GetAuthCodeForDomain #################"
        authcode = n.Domains.GetAuthCodeForDomain("facebook.com")
        print authcode

except NameHttpError, description:
	print NameHttpError
	print description
