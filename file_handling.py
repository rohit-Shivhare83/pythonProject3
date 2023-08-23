# r - open and existing file for READ operation
# w - write operation to open and exiting file
# a - append opertation
# r+ - to read and write the data into file
# w+ - write and read
# a+ - to append read data from file
# x = to open file  in exclusive creation mode for write operation

# note = all above modes are applicable for text

# name - name the file
# mode  - mode in which file is open
# closed - return boolean value indicates
# readable - return boolean value indicates that whether files is readable or not
# writable - return indicator writable or not

# note -  w means over writing the previous file again and again after running
# note - Always Open And then Close the file

# --------------------------------------------------------------------------------

# f = open("abc.txt" , "w" )
# print("name - " ,f.name)
# print("readable ? -  ",f.readable())
# print("writable ? - ",f.writable())
# print("closed -  ? - ",f.closed)
# f.close()
# print("closed -  ? - ",f.closed)


# --------------------------------------------------------------------------



# append

# f= open("abc.txt" ,"a" )
# f.write("Rohit  \n")
# f.write("Pradeep  \n")
# f.write("Rutvij  \n")
# f.write("Sameer  \n")
# f.close()


# ----------------------------------------------------------------------

# read files

# f = open("abc.txt" , "r")
# print(f.read())
# f.close()

# ---------------------------------------------------------------------
# write()
# writelines

# f = open("abc.txt", "a" )
# t = ("rohit\n" , "Pradeep\n" ,"Rutvij\n" , "ayesha\n")
# t2 = {"rohit\n" , "Pradeep\n" ,"Rutvij\n" , "ayesha\n"}
#
# f.writelines(t)
# f.close()

# ------------------------------------------------------------------
# u can make  a file anywhere in your pc make sure u have proper path including
# the slashes //

# f = open("C://Users/admin/Desktop/write.txt","w")
# l = ("rohit" , "Pradeep")
# f.write("Hello I Am Rohit")
# f.writelines(l)
# f.close()

# -------------------------------------------------------------------
# read() - read file
# readline() - read the line
# readlines() - it will read line by line all line
# read(n) - read line with given number of  characters

# f = open("abc.txt","r")
# print(f.read())
# f.close()

# -------------------------------------------------------------------
# readline() - read the line
# f = open("abc.txt","r")
# print(f.readline())
# f.close()

# --------------------------------------------------------------------
# read(n) - read line with given number of  characters
# f = open("abc.txt","r")
# print(f.read(10))
# f.close()

# ----------------------------------------------------------------------
# readlines() - it will read line by line all line
# f = open("C://Users/admin/Desktop/write.txt","r")
# f = open("abc.txt","r")
# lines  = f.readlines(10)
# for i in lines:
#     print(i , end=" ")
# f.close()
# print("checking if my files close or not ? " , f.closed)

# -----------------------------------------------------------------------

# using with and as -
# if we use with we don't need to close the file

# with open("C://Users/admin/Desktop/write.txt","w") as f:
#     f.write("Hello My Name Is Rohit\n")
#     f.write("My Surname Is Shivhare")
#
# print("checking wheather the file is close or not  - ",f.closed)

# ----------------------------------------------------------------------
# tell function - it shows the position of our cursor pointer
# read
# with open("C://Users/admin/Desktop/write.txt","r") as f:
#     print(f.read())
#     # print(f.readline(5))
#
#     print(f.tell())
# ----------------------------------------------------------------------

# seek function - it will take our cursor to a particullar position
# using write

# data = "Rohit Is Great"

# f= open("C://Users/admin/Desktop/write.txt" , "w")
# f.write(data)
# print("cursor is at - " , f.tell())

# with open("C://Users/admin/Desktop/write.txt","r+") as f:
#     print("cursor is at : ", f.tell())
#     f.seek(15)
#     f.write("Person")
#     print(f.tell())
#     print(f.read())
#     f.seek(0)
#     # print(f.tell())
#     # f.write("Hello")
#     # print(f.readline())

# -------------------------------------------------------------------
# check wheather file is exist or not
# import os ,sys
# fName = input("Enter file Name : - ")
# if os.path.isfile(fName):
#     print("File is Exist " , fName)
# else:
#     print(fName,"Does NOt Exist")
#     sys.exit()

# ----------------------------------------------

# read the file if exist
# import os ,sys
# fName = input("Enter file Name : - ")
# if os.path.isfile(fName):
#     print("File is Exist " , fName)
#     f = open(fName , "r")
# else:
#     print(fName,"Does NOt Exist")
#     sys.exit()
#
# print("reading now")
# print(f.read())

# ------------------------------------------------------------

# import csv

# with open("emp.csv ", "w") as f:
#     w = csv.writer(f)
#     w.writerow(["id" , "phone" , "name" , "salary"])
#     n  = int(input("Enter nomber of employess"))
#     for i in range(n):
#         emp_id  = input("enter id")
#         emp_phone  = input("enter phone ")
#         emp_name  = input("enter name")
#         emp_salary  = input("enter salary")
#         w.writerow([emp_id,emp_phone,emp_name,emp_salary])
#
# print("everything is succesfull")


# ----------------------------------------------------------------------
# read()
# readlines()
# readline()
# read(n)
# readable()

# write()
# writlines()
# writable()

# close()
# closed

# seek
# tell


# -----------------------------------------------------------------
# file handling test practices
# read file word by word

# with open("C://Users/admin/Desktop/write.txt", "r") as f:
#     for line in f:
#         for word in line.split(" "):
#             print(word)
# ----------------------------------------------------------------
# f = open("abc.txt" , "r")
# print(f.read())
# f.close()
# -----------------------------------------------------------------





















# f = open("shikha.txt", "a")

# f.write("shikha")
# # print(f.read())
#
# f.close()


# f = open("shikha.txt","w")
# f.write("shikha")
# f.close()
# print("is it close?",f.closed)

# --------------------------------------------------------------------------


# f = open("shikha.txt","w")
# f.write("Rohit")
# print(f.readable())
# print(f.writable())
# f.close()
# print("is it is close?",f.closed)














