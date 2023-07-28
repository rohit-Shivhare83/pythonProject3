# 1 - create ulta pyramide from downside printing the input from user *


# n= int(input("enter your number - "))
# for i in range(n,0,-1):
#     for m in range(n-i):
#         print(" ",end="")
#     for l in range(i):
#         print("*",end=" ")

#     print()

# -------------------------------------------------------------

# 2 write a prog which reads file contains line by line

# f= open("abc.txt","r")
# for line in f.readlines():
#     print(line)

# or

# # print(f.readline())
# # print(f.readline())
# # print(f.readline())

# f.close()

# ----------------------------------------------
# 3 - write a program to randomly select an element from the list

# import random
# list = [1,2,3,4,5,7,8,9,10]
# r = random.choice(list)
# print(r)


# ---------------------------------------------------------

# 4 - write  prog to append a text inta a existing file

# f= open("abc.txt","a")
# f.write("mayur sir")
# f.close()

# ----------------------------------------------------
# 5 - write a prog to extract extension of file

# import os
# file_details = os.path.splitext("C://Users/admin/Desktop/write.txt")
# print(file_details)
# print(file_details[1])


# ---------------------------------------------------------

# 6 - write a prog to reverse of a given number ,  num from user

# n = str(input("enter number : "))

#  print(n[::-1])

# or

# def rev(num):
#     n = len(num)
#     strg = ""
#     while n>0:
#         strg = strg + num[n-1]
#         n = n-1
#     return strg

# l = rev(n)
# print(int(l))

# note - taking into string and then converting into integer

# or

# num = 123456
# rev_num = 0
#
# while num!=0:
#     digit = num%10
#     rev_num  = rev_num *10 +digit
#     num//=10
#
# print(str(rev_num))



