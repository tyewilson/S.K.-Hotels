import bcrypt
import getpass


print(F""" 




-------Welcome to the S.K. Hotels staff portal-------------------


 This portal is only for Admin use to add a user to the systems.


------------------------------------------------------------------




""")


usr = input("Please input staff username: ")
pwd = getpass.getpass("please inpput staff password: ")


    
HashPwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    
with open("StaffData.txt","a") as file:
    file.write(f'{usr}:{HashPwd.decode("utf-8")}\n')