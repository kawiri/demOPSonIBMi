
import pydoc

class Db2foriSettings():

    DATABASES = {
        'Db2fori': {
            'ENGINE': 'ibm_db_django',
            'NAME': 'BAFBKP',
            'USER': 'CR191379',
            'PASSWORD': 'ADMIN123',
            'HOST': '172.17.50.203',
            'PORT': '446',
        },
    }