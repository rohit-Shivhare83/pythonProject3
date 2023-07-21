# for i in range(1,6) :
#     for j in range (1,7):
#         print(j , end=" ")
#     print()
# o/p
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6

# ---------------------------------
# for i in range(1,6) :
#     for j in range (0,i):
#         print(i , end=" ")
#     print()
# o/p
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5
# -------------------------
# for i in range(6,0,-1) :
#     # print(i)
#     for j in range (1,7):
#         print(i , end=" ")
#     print()
# 6 6 6 6 6 6
# 5 5 5 5 5 5
# 4 4 4 4 4 4
# 3 3 3 3 3 3
# 2 2 2 2 2 2
# 1 1 1 1 1 1
# -----------------------------------
# for i in range(5) :
#     # print(i)
#     for j in range (5 , 0 ,-1):
#         print(j , end=" ")
#     print()
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# ------------------------
# for t in range(0,1):
#     print(1)
# for i in range(1,6):
#     for j in range(0,i):
#         print(j , end=" ")
#     for i in range(5,0,-1):
#         print(" " ,end="")
#     print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# -----------------------------------------
# for t in range(0,1):
#     print(1)
# for i in range(1,8):
# print(i)
# for j in range(2,i):
#     print(j , end=" ")
#         i+=j
# for k in range(5,0,-1):
#     print(" " , end = " " )
# print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# --------------------------------
# for i in range(6,0,-1):
#     for k in range(i , 0 ,-1):
#         print(i , end=" ")
#     for j in range(0,5):
#         print(" " ,end=" ")
#     print()
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# ----------------------------------------------
# for i in range(0,6):
#     for j in range(0,i):
#         print(i, end=" ")
#     for k in range( 5 , 0 , -1):
#         print(" ", end=" ")
#     print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5