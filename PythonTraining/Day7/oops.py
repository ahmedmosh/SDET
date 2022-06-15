# Example 1: To create a class and object in python

class MyClass:
    def myfunc(self):  # when a function is created within a class its called a method and it comes with a "self"
        # argument
        pass

    def display(self):
        print("john")


mc1 = MyClass()  # creating an object
mc2 = MyClass()

mc1.display()  # john
mc1. myfunc()

# Example 2: there two types of methods that can be created in a class
# 1. instance method: can be called using an object
# 2. static methods: can be called directly using the class using(@staticmethod)annotation


class MyClass1:
    def m1(self):
        print("this is an instance method")

    @staticmethod  # annotation
    def m2(self, num):
        print(num)


mc = MyClass1()
mc.m1()  # Called using the object.
MyClass1.m2(30, 100)  # Called directly using the class

# Example 3:


class MyClass2:
    a, b = 10, 20  # class variables

    def add(self):
        print(self.a + self.b)  # they can be accessed using the self keyword

    def mul(self):
        print(self.a * self.b)


ko = MyClass2()
ko.add()  # 30
ko.mul()  # 200

# Example 4 : Using global, class and local variables.
i, j = 15, 25  # global variable


class MyClass3:
    c, d, = 10, 20

    def add(self, x, y):  # x, y are local variables.
        print(x + y)
        print(self.c + self.d)  # c, d are class variables
        print(i + j)  # i , j are global variables and can be accessed from anywere


Q = MyClass3()
Q.add(3, 5)

# Example 5:

p, q = 15, 25  # global variable


class MyClass4:
    p, q, = 10, 20

    def add(self, p, q):  # p, q are local variables.
        print(p + q)
        print(self.p + self.q)  # p, q are class variables
        print(globals()['p'] + globals()['q'])  # p , q are global variables and can be accessed from anywere


P = MyClass4()
P.add("good", "boy")

# Example 6: one class can have multiple objects


class MyClass5:

    def display(self, name):
        print('this is a display method')
        print(name)


obj1 = MyClass5()
obj1.display("mosh")

obj2 = MyClass5()
obj2.display("okegwu")

# Example 7 : constructors

class MyClass6:
    def __init__(self):
        print("this is a constructor")
    def m1(self):
        print("hello...")


obj3 = MyClass6()  # invokes constructors automatically
obj3.m1()  # methods are called explicitly using the object

# Example 8 :


class MyClass7:
    name = "john"

    def __init__(self, name):  # constructors can take arguments also
        print(name)
        print(self.name)


mo = MyClass7(5)  # passes parameter to the constructor

# Example 9 :
# req: emp
#     constructor: eid, ename, esalary
#     display(): print eid, ename & esal


class Emp:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print(self.eid, self.ename, self.esal)


empl = Emp(125, "mosh", 350000)
empl.display()

