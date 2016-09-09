# -*- coding: utf-8 -*-

# method 1: use __new__
class Singleton(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			orig = super(Singleton, cls)
			cls._instance = orig.__new__(cls, *args, **kwargs)
		return cls._instance

a = Singleton()
a.first_arg = 1
b = Singleton()

print a == b
print a is b
print id(a) == id(b)


# method 2: use decorator
def singleton(cls, *args, **kwargs):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance

@singleton
class myClass:
    name = 1

a = myClass()
b = myClass()
print a == b
print a is b
print id(a) == id(b)


#method 3: use import
class myClass:
    name =1

my_class = myClass()

from singleton import my_class

a = my_class
b = my_class
print a == b
print a is b
print id(a) == id(b)