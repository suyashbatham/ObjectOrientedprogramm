class Person:
    # attribute  (data is attribute)
    species = "Home Sapiens" # class attribute  and it is globle
    # methods
    def __init__(self,name,color):  # this name and color is a local variable
        self.name = name
        self.color = color


    def info(self): # self is a default argument to crate a class methods
         print("A preson Can walk")
    # a walk is a method within the class and function outside the class
    def sleep(self):
        print("A preson can sleep")

# make an objects if you want to use class
john = Person() # instanciate the person class
# john.walk()
# john.sleep()
# print(john.species)
janie = Person()
print(janie.species)



