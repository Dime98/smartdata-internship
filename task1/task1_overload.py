class A:
    def __init__(self):
        pass

    def overload_method(self, arg1):
        print("class A")

class B(A):
    def overload_method(self, arg1, arg2, arg3):
        print("class B")

a = A()
a.overload_method(1)
b = B()
b.overload_method(1,2,3)

