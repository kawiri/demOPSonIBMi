import os
import pyodbc
import getpass
from Color import *

try:
    Db2connection = pyodbc.connect('DSN=DSN_Db2iBKP') #DSN IBM i Access Driver
    cs = Db2connection.cursor()
    cu_username = getpass.getuser()
    nw_username = input('Username (leave blank to use {} ): ' .format(cu_username))
    if nw_username == '':
        nw_username = cu_username

    nw_email = input('Email : ')
    while True:
        nw_pwd1 =  getpass.getpass('Password : ')
        nw_pwd2 =  getpass.getpass('Password (again) : ')
        if nw_pwd1 != nw_pwd2:
            print(Base.FAIL,"Error: Your passwords didn't match.", Base.END)
        else:
            cs.execute('{CALL SP_INSERT_SUPERUSER(?,?,?)}',(nw_username, nw_email, nw_pwd1))   
            print(Formatting.Bold,"Superuser created successfully.", Formatting.Reset)
            break
except pyodbc.Error as err:
    print('Db2i Create Super User Error : {}'.format(err))
finally:
    if not cs is None:   
        cs.close
    if not Db2connection is None:
        Db2connection.close
