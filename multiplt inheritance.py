class Foo:
    def foo_method(self):
        print("this is foo method")

class Bar:
   def bar_method(self):
       print("This is a bar method")
class FooBar(Foo,Bar):
    def foo_method(self):
        super(FooBar,self).foo_method()
        print("this is foobar method")

fb = FooBar()
print(fb.foo_method())
