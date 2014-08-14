#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>


try:
    import json
except ImportError:
    import simplejson as json

class Manifest(object):
    def __init__(self):
        self._manifest = None

    def data(self):
        return self._manifest

    def load(self, file_name):
        pass

    def save_to(self, file_name):
        pass
