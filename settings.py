# -*- coding: utf-8 -*-
__author__ = 'yijingping'

DATABASE = {
        'HOST': '127.0.0.1',
        'NAME': 'poormining',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {
            'charset': 'utf-8',
        }
}
MONGODB = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'NAME': 'poormining',
        'USER': '',
        'PASSWORD': ''

}


## Import local settings
try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' in the directory containing %r.\n" % __file__)
