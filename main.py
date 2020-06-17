class Person():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def info(self):
        print(self.name)
    def sleep(self):
        print("{} is slepping".format(self.name))
    def rename(self,new_name):   # manipulating object attribute
        self.name = new_name
        print("Now my new name is {} ".format(self.name))


# john = Person("suyash","red")
# john.sleep()
# john.info()

# sara = Person('Sara','Brown')
# sara.sleep()
# sara.rename("suyash")




# bound , unbound and static methods
class A:
    @classmethod   # it is used not to instatiate the class object
    def f(self,x):      # self is argument
        print(2*x)
    @staticmethod             # both class and static ,ethod are similar
    def g(name):               # but self is not used
        print("Hello,%s"%name)


# print(A.f)
# a = A()
# a.f(2)

A.f(2)  #4    # using @class Method  class the method directly
a = A()
a.g("Suys")