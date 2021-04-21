"""Database methods"""
from Color import *
import pyodbc

class DbSettings:
    """Database info"""
    DATABASES = {
        'Db2fori': {
            'ENGINE': 'ibm_db_django',
            'NAME': 'DBNAME',
            'USER': 'USUARIO1',
            'PASSWORD': 'XXXXXX',
            'HOST': 'XXX.XX.XX.XXX',
            'PORT': '446',
        },
    }    
    
    """Methods"""
    def Validate(self):
        """Si existen la tablas en el schema, las elimina antes de crearlas."""
        try:
            print(Color.F_Cyan,"Operations to perform:",Color.F_Default)
            print(Formatting.Bold,"    Apply all migrations: ibm_db2fori, user, profile", Formatting.Reset)
            print(Color.F_Cyan,"Running migrations:",Color.F_Default)
            Db2connection = pyodbc.connect('DSN=DSN_Db2iBKP') #DSN IBM i Access Driver
            c1 = Db2connection.cursor()
            c1.execute("CALL SP_DROP_TABLES")
        except Db2connection.Error as err:
            print('Db2 Drop Tables Error : {}'.format(err))        
        finally:
            if not c1 is None:
                c1.close()
            if not Db2connection is None:
                Db2connection.close()

    def Adjust(self):
        """ Actualiza el CCSID de las columnas de las tablas. """
        try:
            Db2connection = pyodbc.connect('DSN=DSN_Db2iBKP') #DSN IBM i Access Driver
            c1 = Db2connection.cursor()
            c1.execute("CALL SP_ALTER_CCSID")
            print(Color.F_Cyan,"Applying user, profile... OK",Color.F_Default)
        except pyodbc.Err as err:
            print('Db2 Alter CCSID Error : {}'.format(err))    
        finally:
            if not c1 is None:
                c1.close()
            if not Db2connection is None:
                Db2connection.close()
