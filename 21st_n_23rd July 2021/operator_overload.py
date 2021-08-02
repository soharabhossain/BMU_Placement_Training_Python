

# Python Program illustrate how to overload an binary + operator
 
class A:
    def __init__(self, arg):
        self.a = arg
 
    # Adding two objects (to overload the + operator)
    def __add__(self, obj):
        return self.a + obj.a

print(dir(A))


ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)

ob3 = A("BMU")
ob4 = A("Gurgaon")
print(ob3 + ob4)




class foo:
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        if self.x < other.x:
            return False
        else:
            return True

a = foo(2)
b = foo(3)
print(a < b)

