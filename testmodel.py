from models import *

class User(Model):
    id = IntegerField(notnull=True)
    name = StringField(notnull=True)
    email = StringField()
    password = StringField(notnull=True)

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print u._check_essential()
u2 = User(id=12345, email='test@orm.org', password='my-pwd')
# print u2._check_essential()	
u3 = User(id=12345, name='Michael', password='my-pwd')
print u3._check_essential()
