# # PASSWORD GNERATOR
import random
# import re

length_from_user = int(input("Enter length of your Password  ==> "))
int_1 = ["1","2","3","4","5","6","7","9","0" , "@","#","$","%","^","&","*",
         "a","q","w","e","r","t","y","u","i","o","","","","","","","","","","","","","","","",""]

if length_from_user > 4 and length_from_user < 13:
    t = ""
    for i in range(0,length_from_user):
        r = random.choice(int_1)
        t = t+r
    print(t)
else:
    print("enter approciate lengeth for your password from 5 to 12")

