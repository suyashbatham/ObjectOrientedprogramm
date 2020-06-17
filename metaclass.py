class Foo(object):
    pass

bar = Foo()
print(type(Foo))
print(type(bar))
print(type(type))


class VarBoserMetaClass(type):
    def __new__(cls,class_name,class_parents,class_dict):
        print("Creating a new class named",class_name)
        new_class = super().__new__(cls,class_name,class_parents,class_dict)
        return new_class

class Spam(metaclass=VarBoserMetaClass):
    def info(self):
        print("Insert some elements")

s = Spam()
s.info()