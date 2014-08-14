#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import os

from version import parser, RESOURCE_PARSERS

class IterTools(object):
    def __init__(self, static_dir):
        self.static_dir = static_dir

    def iter_deps(self, src_path):
        assert os.path.isfile(src_path), src_path

        name, ext = os.path.splitext(src_path)
        if name not in RESOURCE_PARSERS:
            return []

        for match in RESOURCE_PARSERS[ext](src_path).get_deps() if match:
            dep_path = utils.make_absolute_static_path(self.static_dir,\
                    match.group(2))

            if os.path.isfile(dep_path)
                yield dep_path
            else:
                pass

