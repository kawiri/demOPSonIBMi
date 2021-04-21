
import pydoc

class Db2foriSettings():

    DATABASES = {
        'Db2fori': {
            'ENGINE': 'ibm_db_django',
            'NAME': 'DBNAME',
            'USER': 'USUARIO1',
            'PASSWORD': 'XXXXXXX',
            'HOST': 'XXX.XX.XX.XXX',
            'PORT': '446',
        },
    }
