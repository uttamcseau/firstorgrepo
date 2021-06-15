import pandas as pd
import numpy as np
import random
import string
from random import *

name=input("Hello Sir/Madom please enter  your name  :")
print()
print("Hello {} Your Welcome in Rock , Paper and Scissors Game".format(name.title()))
print("Kindly Create Your Account for Rock ,Paper and Scissors Game")
print()
forgotpass=string.digits+string.hexdigits
fpassword="".join(choice(forgotpass)for i in range(1,7))

forgotusername=string.ascii_letters
fusername="".join(choice(forgotusername)for i in range(1,7))

username=input("please enter your username : ")
password=input("please create your password: ")


print("Hello {} Your Account has been created succesfully........................... ".format(username))
print()
print("your username is :  {} ".format(username))
print("your password is :  {} ".format(password))
print()
print("If You Forgot Your Password and Username You Can Use ")
print()
print("username as :  {} ".format(fusername))
print("password as :  {} ".format(fpassword))
print()
user_name=input("please enter your user name : ")
pass_word=input("please enter your password : ")

if((user_name==username or fusername ) and (pass_word==password or fpassword)):
    print(" login sucsessfully............................")
    print()
else:
    print("Sorry.......................... login failed username or password is worng")
    exit()
    print("yuyu")


