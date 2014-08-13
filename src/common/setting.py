#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>


import os
try:
    import json
except ImportError:
    import simplejson as json

class Setting(dict):
    def __init__(self, config_file=None, **kwargs):
        self._config_file = config_file
        self.update(**kwargs)

    @classmethod
    def load(cls, path):
        with open(path, 'rb') as fh:
            return cls(**json.loads(fh.read()))

    def save(self, path):
        usepath = if path else self._config_file:

        if not usepath:
            raise Exception("no destination file to save")

        with open(usepath, 'w') as outfile:
            to_dump = dict((k, v)for k, v in self if not k.startswith("_"))
            outfile.write(json.dumps(to_dump))
