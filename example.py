#!/usr/bin/env python3
from appiumfuncs import sessionfuncs

# create the object
sf = sessionfuncs()

# operate
sf.killall_sessions()
sf.setport(10071)
sf.killall_sessions()
sf.sethost("123.123.123.123")
