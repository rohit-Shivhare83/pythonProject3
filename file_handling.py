# r - open and existing file for READ operation
# w - write operation to open and exiting file
# a - append opertation
# r+ - to read and write the data into file
# w+ - write and read
# a+ - to append read data from file
#
# x = to open file  in exclusive creation mode for write operation

# note = all above modes are applicable for text
# name - name the file
# mode  - mode in which file is open
# closed - return boolean value indicates
# readable - return boolean value indicates that whether files is readable or not
# writable - return indicator writable or not

# --------------------------------------------------------------------------------
# f = open("abc.txt" , "w" )
# print("name - " ,f.name)
# print("readable ? -  ",f.readable())
# print("writable ? - ",f.writable())
# print("closed -  ? - ",f.closed)
# f.close()
# print("closed -  ? - ",f.closed)
#

# --------------------------------------------------------------------------

# note -  w means over riting the previous file again and again after running
# note - Always Open And then Close the file

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
# u can make  a file anywhere in your pc make sure u have proper path including the slashes //

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
# print("cheking if my files close or not ? " , f.closed)


# ----------------------------------------------------------------------
# read()
# readlines()
# readline()
# read(n)

# write()
# writlines()

# close()
# closed





