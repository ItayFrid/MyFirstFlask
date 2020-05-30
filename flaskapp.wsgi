#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/MyFirstFlask/")

from MyFirstFlask import app as application
application.secret_key = '\xcd\x0c\xea\x17q\xb9\xcb\xbb\xa7:\x97\xd6x\x10\x01\xef\xe8\xd2\x90\xb3[\xb0\x92\xda'