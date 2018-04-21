class Field(object):
    def __init__(self, column_type, notnull=False):
        self.column_type = column_type
        self.notnull = notnull
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.column_type.__name__)
    def accept(self, val):
        return isinstance(val, self.column_type)

class StringField(Field):
    def __init__(self, notnull=False):
        super(StringField, self).__init__(type("adfdas"), notnull)

class IntegerField(Field):
    def __init__(self, notnull=False):
        super(IntegerField, self).__init__(type(1), notnull)

class ListField(Field):
    def __init__(self, itemType, notnull=False):
        assert(isinstance(itemType, Field))
        self.itemType = itemType
        super(IntegerField, self).__init__(type([]), notnull)
    def accept(self, val):
        if not isinstance(val, self.column_type):
            return false
        for item in val:
            if not itemType.accept(val):
                return false
        return true
