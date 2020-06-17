class Duck:
    def quack(self):
        print("Qxhjscdcsd")

    def feathers(self):
        print("The duck has  white feathers")


class Person:
    def quack(self):
        print("the person can imiate duck")

    def feathers(self):
        print("The person takes a feather from the ground")

    def name(self):
        print("Suyash Batham")


def in_the_forest(obj):
    obj.quack()
    obj.feathers()

donald = Duck()
matt = Person()
in_the_forest(donald)
print("----------------------------------------------------------------------------")
in_the_forest(matt)