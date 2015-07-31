# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('C:\\Program Files (x86)\\Google\\google_appengine\\lib\\django-1.5\\')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tatdjangotest.settings")
