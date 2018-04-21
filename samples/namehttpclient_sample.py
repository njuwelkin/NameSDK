import sys
sys.path.append("..")

import namehttpclient

n=namehttpclient.NameHTTPClient(username="account", token="a3d9f8d...............", host=namehttpclient.NAMEHOST)


# hello
#r = n.v4.hello.get()
#print(r.__dict__)

#
# Domains
#

# ListDomains, GET /v4/domains
#r = n.http_get("/v4/domains")
#print(r.__dict__)


# GetDomain, GET /v4/domains/{domainName}
#r = n.http_get("/v4/domains/hai-tang.com")
#print(r.__dict__)

# GetAuthCodeForDomain, GET /v4/domains/{domainName}:getAuthCode
#r = n.http_get("/v4/domains/hai-tang.com:getAuthCode")
#print(r.__dict__)

# CheckAvailability, POST /v4/domains:checkAvailability
#r = n.http_post("/v4/domains:checkAvailability", body='{"domainNames":["facebook.com"]}')
#print(r.__dict__)



# Search, POST /v4/domains:search
r = n.http_post("/v4/domains:search", body='{"keyword":"facebook", "timeout":3000, "tldFilter":["com"]}')
print(r.__dict__)

