import settings
from Domains.models import *

test_str = '{"domainName":"biubiu.org","locked":true,"autorenewEnabled":true,"expireDate":"2020-12-14T05:06:50Z","createDate":"2012-12-14T05:06:50Z"}'

d = Domain.from_json(test_str)
