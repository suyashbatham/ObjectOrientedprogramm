class A:
    def __init__(self,a,b):   # magic method
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a,self.b + other.b

    def __sub__(self, other):
        return self.a - other.a,self.b - other.b

#(1,2) --> vectors1
#(2,4) --> vectors2
# for vector addition(1+2,2+4)

obj1 = A(1,2)
obj2 = A(2,4)
print(type(obj1))
print(type(obj2))
print(obj1+obj2)
print(obj1-obj2)
print(obj1+obj2)
print(obj1-obj2)



class A:
    def __init__(self,a):
        self.a = a


    def __lt__(self, other):
        if(self.a < other.a):
            return "obj1 is lesser than obj2"
        else:
            return "obj2 is less than obj1"

    def __eq__(self,other):
        if(self.a == other.a):
            print("Both are equal")
        else:
            print("Both are not equal")

obj1 = A(2)
obj2 = A(3)
print(obj1<obj2)
print(obj1==obj2)