# Exception handling
# ------------------------------------------
# try
        # actual logical
# except
        #error

# ----------------------------------------
# try
#       ....
# except
#       ....
# except
#       ...
# --------------------------------------
# try:
#     try:
#           ....
#     except:
#           ....
# except:
#         ....
# except:
# ----------------------------------------------
# try:
#    ......
# except:
#   .....
# finally:

# -----------------------------------------------

# there are two types of error:-

# Syntax Error  or syntactical error : erroe accurs because of syntax error
# RunTime Error : someone enters wrong type of input or programming logic or memory problems

# ------------------------------------------------

# print(hello)
# op : NameError: name 'hello' is not defined. Did you mean: 'help'?
# # exit code 1 :  means not ended naturally .

# ---------------------------------------------------
# try:
#     print(hello)
# except NameError:
#     print("enter proper names")

# op : enter proper names
# exit code 0 : 0 means naturally ended

# --------------------------------------------------
# try:
#     a = int(input("kachrya chukicha number taku nko : "))  # input = 10
#     b = int(input("number taak re : "))  ## input = jsdvbj
#     c=a+b
#     print(c)
#
# except NameError:
#     print("chukicha input kashala taklas re *****a ")
#
# except ValueError:
#     print("chukicha input kashala taklas re *****a ")

# op :
# kachrya chukicha number taku nko : 10
# number taak re : 20nfgdg
# chukicha input kashala taklas re *****a

# ------------------------------------------------------

# try:
#     a = int(input("kachrya chukicha number taku nko : "))  # input = 10
#     b = int(input("number taak re : "))  ## input = jsdvbj
#     c=a/b
#     print(c)
#
# except ArithmeticError as AE:
#     print("this is parent error for division error or error--> cant divide with zero "  , AE)
#
# except ZeroDivisionError as zde :
#     print("error--> cant divide with zero" ,zde)
#
# except NameError:
#     print("chukicha input kashala taklas re *****a ")
#
# except ValueError:
#     print("chukicha input kashala taklas re *****a ")

# ----------------------------------------------------------
# try:
#     a = int(input("kachrya chukicha number taku nko : "))  # input = 10
#     b = int(input("number taak re : "))  ## input = 0
#     c=a/b
#     print(c)

# writing all error at a single line no need to repeat except again and again
# except (ValueError , NameError , ZeroDivisionError) as msg:
#     print("handling any one which comes as error ---> " , msg)

# ------------------------------------------------------------
# by dafault error
# dafault except is always at end

# try:
#     a = int(input("kachrya chukicha number taku nko : "))  # input = 10
#     b = int(input("number taak re : "))  ## input = 0
#     c=a/b
#     print(c)
#
# except ValueError:
#     print("chukicha input kashala taklas re *****a ")

# ------------------------------------------------
# text="what is your name ?"
# if ("+" in text):
#     print("yes, ? is present")
# else:
#     print("? is not in present")


# ---------------------------------------------------
# import os
#
# try :
#     print("try")
#     os._exit(0)
# except NameError:
#     print("except")
# finally:
#     print("finally")
