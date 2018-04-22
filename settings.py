import os
import sys
sys.path.append(os.path.realpath(__file__))



from Domains.apis import Domains
modules = {
    "Domains": Domains
}
