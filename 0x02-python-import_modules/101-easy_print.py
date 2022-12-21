#!/usr/bin/python3

import builtins

builtins.__dict__['_'] = lambda x: builtins.__dict__['print'](x, end="")

_("#pythoniscool\n")
