# class AttributeDict(dict):
#    def __getattr__(self, attr):
#        return self[attr]
#    def __setattr__(self, attr, value):
#        self[attr] = value


class objdict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)