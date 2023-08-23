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

b = 10

class test:

    c =20
    def __init__(self):
        self.a = 10

    def emp_1(self):
        self.e = 30
        print(self.a)


em = test()
print(em.a)
print(b)
print(em.c)






