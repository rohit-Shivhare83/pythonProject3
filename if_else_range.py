# for i in range (10):
#     if i==7:
#         print("Now you are at 7")
#         break
#     print(i)
# -----------------------------------------
# cart = [10,20,500,600,70,40]
# for items in cart:
#     if items>500:
#         print("You need permission to place order")
#         break
#     print(items)

# --------------------------------------------
# cart = [10,20,500,600,70,40]
# for items in cart:
#     if items>499:
#         print("You need permission to place order")
#         continue
#     print(items)
#

# 0-----------------------------------------------
#wap to print odd numbers i the range od 0-9 using continue
#
# for i in range(10):
#     if i % 2 !=0 :
#         print("this is odd number")
#         continue
#     print(i)

# for i in range(4):
#     for j in range(4):
#         print("#",end= " ")
#     print()

# for i in range(10):
#     for j in range(i+1):
#         print("*" , end="")
#     print()
# -------------------------------
# n=int(input("enter the value "))
# for i in range(1,n):
#     for j in range(i):
#         print("*" ,end="")
#     print()

# ----------------------------
# n=int(input("enter the value "))
# for i in range(n):
#     for l in range(1,n-i):
#         print(" " ,end="")
#     for j in range(1,2*i):
#         print("*" ,end="")
#     print()


# for i in range(1,6 , 2):
#
#     # for space
#
#     for j in range(1,6-i):
#         print(" ",end = "")
#
#     # for printing star
#
#     for l in range (i):
#         print(l ,end = " ")
#
#     print()