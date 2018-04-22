class Field(object):
    def __init__(self, column_type, notnull=False):
        self.column_type = column_type
        self.notnull = notnull
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.column_type.__name__)
    def accept(self, val):
        return isinstance(val, self.column_type)

class StringField(Field):
    def __init__(self, acceptunicode = True, notnull=False):
        self.acceptunicode = acceptunicode
        super(StringField, self).__init__(type("adfdas"), notnull)
    def accept(self, val):
        return isinstance(val, self.column_type) or (self.acceptunicode and isinstance(val, type(u"asdf")))

class IntegerField(Field):
    def __init__(self, notnull=False):
        super(IntegerField, self).__init__(type(1), notnull)

class FloatField(Field):
    def __init__(self, notnull=False):
        super(FloatField, self).__init__(type(3.14), notnull)
    def accept(self, val):
        return isinstance(val, self.column_type) or isinstance(val, int)

class BoolField(Field):
    def __init__(self, notnull=False):
        super(BoolField, self).__init__(type(True), notnull)

class ListField(Field):
    def __init__(self, itemType, notnull=False):
        assert(isinstance(itemType, Field))
        self.itemType = itemType
        super(ListField, self).__init__(type([]), notnull)

#    def accept(self, val):
#        if not isinstance(val, self.column_type):
#            return False
#        for item in val:
#            if not self.itemType.accept(val):
#                print "%s not accept %s", self.itemType, item
#                return False
#        return True

class DictField(Field):
    def __init__(self, notnull=False):
        super(DictField, self).__init__(type(1), notnull)
