from field import *

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return super(ModelMetaclass,cls).__new__(cls, name, bases, attrs)
        mappings = dict()
        essentials = []
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                #print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
                if v.notnull:
                    essentials.append(k)
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name.lower()
        attrs['__mappings__'] = mappings
        attrs['__essentials__'] = essentials
        return super(ModelMetaclass,cls).__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        if self.__class__.__mappings__.has_key(key):
            try:
                return self[key]
            except KeyError:
                raise AttributeError(r"'Model' object has no attribute '%s'" % key)
        else:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        if self.__class__.__mappings__.has_key(key):
            if self.__class__.__mappings__[key].accept(value):
                self[key] = value
            else:
                raise AttributeError(r"'%s' is not valid to %s" % (value, self.__class__.__mappings__[key]))
        else:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def _check_essential(self):
        for key in self.__class__.__essentials__:
            if not self.has_key(key):
                raise AttributeError(r"attribute '%s' is required." % key)
        

    # TODO: add a constructor from dict

class ModelField(Field):               # dict field
    def __init__(self, model_class, notnull=False):
        assert(issubclass(model_class, Model))
        super(IntegerField, self).__init__(model_class, notnull)
