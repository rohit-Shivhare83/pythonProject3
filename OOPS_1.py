# class employee:
#     def __init__(self):
#         self.name = "rohit"
#         self.id = 90027932
#         self.phone = 8381030645
#         print(self.name , self.id , self.phone)


# l = employee()
# print(l.__class__)
# print(l.__dict__)


# ===================================================
# class employee:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = self.a+self.b
#         print("hello world => " , self.c)
#
#     def empl2(self):
#         self.d = 10290
#
# e = employee()
# e.empl2()
# print(self.d)
# print(e.a)
# print(e.b)
# print(e.c)
# e.x = 1025
# print(e.x)

# ============================================


# class test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 350
#         self.d = 40
#     def emp_1(self):
#         self.e = 30
#         del self.a
#
# em = test()
# print(em.__dict__)
# em.emp_1()
# del em.d
# print(em.__dict__)
#
#


# =========================================

# b = 10
#
# class test:
#
#     c =20
#     def __init__(self):
#         self.a = 10
#
#     def emp_1(self):
#         self.e = 30
#         print(self.a)
#
#
# em = test()
# print(em.a)
# print(b)
# print(em.c)

# -==========================================================
# decorators - extending the functinality of class and methods.
# b = 10
#
# class test:
#
#     c = 20
#     def __init__(self):
#         self.a = 10
# em = test()
#
# t1 = test()
# t2 = test()
#
# print("t1 : " , t1.c , t1.a)
# print("t2 : " , t2.c , t2.a)
#
# print("t1 changed " , t1.c  , t1.a)
# print("t2 changed " , t2.c  , t2.a)
#
# test.c = 800
# t1.a = 400
#
# print("t1 changed " , t1.c  , t1.a)
# print("t2 changed " , t2.c  , t2.a)


# =====================================================

# class animal:
#     legs = 4
#     @classmethod
#     def walk(self , name):
#         print('{} walks with {} legs'.format(name , self.legs))
#
# animal.walk("cat")
#

# ==========================================

#
# classmethod
# staticmethod

# class test():
#     a=122
#     def __init__(self):
#         test.a = 20
#
#     @classmethod
#     def m1(cls):
#         cls.a = "one piece"
#         test.c = "naruto"
#     # @classmethod
#     def m2(self):
#         test.a = "rohit"
#
#     def m3(self):
#         test.a = "it"
#         self.y = "cs"
#
# t= test()
# print(t.a)
#
# t.m1()
# print(t.a)
#
# t.m2()
# print(t.a)


# ============================================== #
# class ShivhareRohit:
#     @staticmethod
#     def add(x,y):
#         print(x+y)
#     @staticmethod
#     def sub(x,y):
#         print(x-y)
#     def mul(x,y):
#         print(x*y)
#     def div(x,y):
#         print(x/y)
#
# # l= ShivhareRohit()
# ShivhareRohit.add(10,29)
# ShivhareRohit.sub(10,29)
# ShivhareRohit.mul(10,29)
# ShivhareRohit.div(10,29)

# ===================================================

# class employee:
#     def __init__(self,id,name,sal):
#         self.name = name
#         self.id = id
#         self.sal = sal
#     def display(self):
#         print("emp id :" , self.id)
#         print("emp name :" , self.name)
#         print("emp salary :",self.sal)
# class test:
#     def modify(pc):
#         pc.sal = pc.sal+1000
# d = employee(10,"Rohit",300)
# d.display()
# e = employee(20,"pradeep",1)
# test.modify(e)
# e.display()


# ============================================================







