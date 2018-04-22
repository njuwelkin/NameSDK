from field import *
import json

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
        print type(kw)
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
        self._set_attr(key, value)

    def _set_attr(self, key, value):
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

    @classmethod        
    def from_json(cls, str):
        d = json.loads(str)
        return cls.from_dict(d)

    @classmethod        
    def from_dict(cls, d):
        ins = cls()
        for k, v in d.iteritems():
            if cls.__mappings__.has_key(k):
                tp = cls.__mappings__[k]
                if tp.column_type != type([]) or (not isinstance(tp.itemType, ModelField)):
                    ins._set_attr(k, v)
                else:
                    l = []
                    if isinstance(v, type([])):
                        for item in v:
                            l.append(tp.itemType.column_type.from_dict(item))
                            
                    ins._set_attr(k, l)
        return ins
            

class ModelField(Field):               # dict field
    def __init__(self, model_class, notnull=False):
        assert(issubclass(model_class, Model))
        super(ModelField, self).__init__(model_class, notnull)
