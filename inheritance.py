class BaseClass:
    def walk(self):
        print("I am Walking")
class DerivesClass(BaseClass):
    def swim(self):
        print("I am Swimming")

d = DerivesClass()
d.walk()
d.swim()


class Rectangle():
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def preimeter(self):
        return 2*(self.w+self.h)


class Square(Rectangle): # base class
    def __init__(self,s):
        super(Square,self).__init__(s,s) # this is a init method of rectangle
        self.s = s

s = Square(5)
print(s.area())
print(s.preimeter())


# Monkey Patching : to Add some functionality into class
class A:
    def __init__(self,num):
        self.num = num

    def add(self,a):
        print(self.num+a)

def get_num(self):
    return self.num

A.get_num = get_num #MP
foo = A(43)
print(foo.get_num())
bar = A(45)
print(bar.get_num())
