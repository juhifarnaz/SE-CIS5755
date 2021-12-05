# Python Program illustrate how
# to overload an binary + operator
 
class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
obj1 = A(7)
obj2 = A(8)
obj3 = A("Group Project")
obj4 = A("Code Management")
 
print(obj1 + obj2)
print(obj3 + obj4)