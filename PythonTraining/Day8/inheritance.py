# Example 1:
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from B")
#
#
# bobj = B()
# bobj.m1()   # this is m1 method from class A
# bobj.m2()   # this is m2 method from class B

# Example 2: single inheritance

class C:
    x, y = 10, 20
    def m3(self):

        print(self.x + self.y)


class D(C):
    a, b = 100, 200

    def m4(self):
        print(self.a - self.b)


dobj = D()
dobj.m3()  # 30
dobj.m4()  # -100

# Example 3 : Multi level inheritance: combination of multi single inheritances


class E:
    i, j = 5, 2

    def m5(self):
        print(self.i + self.j)


class F(E):
    p, m = 200, 100

    def m6(self):
        print(self.p - self.m)


class G(F):
    s, t = 10, 20

    def m7(self):
        print(self.s * self.t)


alex = G()
alex.m7()  # 200
alex.m6()  # 100
alex.m5()  # 7

# Example 4: Hierarchy inheritance


