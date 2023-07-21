# 1
# max number of three

# a=1
# b=3
# c=10

# def add(a,b,c):
#     print(max(a,b,c))
# add(a,b,c)

# ---------------------------------------------------
# 2  reverse string
# l = "rohit"
# print(l[::-1])

# def rever_string(str):
#     string = ""
#     n = len(str)
#     while n>0:
#         string += str[n-1]
#         n-=1
#     return string
#
# print(rever_string("welcome"))



# -------------------------------------------------
# 3 factorial
# def fact():
#     sum=1
#     i=0
#     while i <10:
#         i+=1
#         sum*=i
#         print(sum)
# fact()
# op
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

# ----------------------------------------------

# 4 list and return

# list = [1,2,3,4,5,6,7,8,9]
#
# def li(l):
#     return l
# print(li(list))

# ------------------------------------------
# def unique_value(list):
#     x=[]
#     for i in list :
#         if i not in x:
#             x.append(i)
#     return x
#
# print(unique_value([1,22,3,3,4,4,5,5]))



# op [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ------------------------------------------

# 5 function inside function
# def outer( a ):
#     b=10
#     def inner():
#         nonlocal b
#         return a+b
#     return inner()
#
# print(outer(10))


#---------------------------------------
# 6 sum of all list
# list = [ 1,2,3,4,5]
# sum =0
# for i in list:
#     sum+=i
#     print(sum)
# op
# 1
# 3
# 6
# 10
# 15

# ----------------------------------------------------
# 7 largest number fromt list
# list = [1,2,3,4,5,688,35,7568]
# for i in list:
#     k = max(list)
# print(k)

# n= len()
# a=list.sort()
# n=len(a)
# # print(a)
# for i in a:
#     print(a[n-1])




# op
# 7568

# -----------------------------------------------
# 8 copy list
# list = [1,2,3,4,5,688,35,7568]
# b=list.copy()
# print(b)

# op
# [1, 2, 3, 4, 5, 688, 35, 7568]



# ---------------------------------------------------
# 9
# list =[1,2,5,8,9,10,11]
# list.remove(1)
# list.remove(9)
# list.remove(10)
# print(list)
# op
# [2, 5, 8, 11]


# -------------------------------------------------
# 10 diffrence list
# list = [1,2,3,4,5,688,35,7568]
# list2 = [33,1,5,77,7568]


# ---------------------------------------------------
# 11 tuple last
# t = (1,2,3,4,5,6,7,8,9)
# print(t[-4])
# op
# 6

# -------------------------------------------------
# 12 dictionary keys
# dic = {1:"rohit",2:"pradeep"}
# print(dic)
# dic.keys()
# print(dic.keys())
# dic.keys(2)
# print(type(dic))

# ------------------------------------------------
# 13
# crete new dict
# dic1={1:"rohit"}
# dic2={2:"pradeep"}
# dic3 = dic1 + dic3
# # dic3 =
# print(dic3)

# -------------------------------------------------
# 14
# sum of all items in dictionary
# dic = {1:100 , 2:200 , 3:300 ,4:400 , 5:500}
# print(sum(dic.values()))

# mul=1
#
# for i in dic:
#     mul = mul*dic[i]
# print(mul)
# dic.values()

# ----------------------------------------------------
# 17 even numbers

# list= [101, 102, 103, 111, 112, 113, 114, 115, 202, 203, 204, 401, 402]
# for i in list :
#     if (i % 2 == 0):
#         print(i)

# op
# 102
# 112
# 114
# 202
# 204
# 402



# ------------------------------------------------
# 18
# create tuple
# tuple= ( 1,2,3,4,5,6,7,8,9,10)
# print(type(tuple))
# print(tuple)


# ---------------------------------------------------
# 19
# given range falls
# a= int(input("enter your number to check it fall within a range : "))
# list = [1,2,3,4,5,6,7,8,9,10]
#
# if  list.__contains__(a):
#     print("yes... it fall under range ")
# else:
#     print("no")


# ----------------------------------------------------
# def ran(a):
#     if a in range(1,10):
#         print("yes")
#     else:
#         print("no")
# a = int(input("enter : "))
# ran(a)



# op
# yes... it fall under range


# -----------------------------------------------
# 20
# def sqr():
#     i=0
#     sqr = 0
#     for i in range(1,31):
#         # print(i , "")
#         sqr = i*i
#         i+=i
#         print(sqr )
# sqr()

# def sqr ():
#     l = list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l)
# sqr()

# op
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361
# 400
# 441
# 484
# 529
# 576
# 625
# 676
# 729
# 784
# 841
# 900


# -----------------------------------------------------------
# lambda function
# d = lambda a : a*a
# print(d(10))

# write a program to calculate biggest of given number
# d = lambda a,b: a if a>b else b
# print(d(10,20))
# how to use

# -------------------------------------------------
# write lambda fun to calc average of three numbers

# ave = lambda a,b,c : (a+b+c)/3
# print(ave(1,2,3))

# l =[1,2,3,4,5,6,7,8,9,10]
# s= list(filter((lambda l : l%2==0  ),l))
# print(s)

# b = lambda l : l%2==1
# print(b(5))
# l =[1,2,3,4,5,6,7,8,9,10]
# a = list(filter(b , l ))
# print(a)

