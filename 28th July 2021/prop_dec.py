class person:
    def __init__(self):
        self.__name=''

    @property
    def name(self):
        return self.__name

    # To mark this method as a setter method for the name property,
    # the @name.setter decorator is applied. 
    @name.setter
    def name(self, value):
        self.__name=value

    @name.deleter
    def name(self, value):
        print('Deleting..')
        del self.__name


p = person()
p.name = 'Soharab'
print(p.name)

del p.name
print(p.name) 
