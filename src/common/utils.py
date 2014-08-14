#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import os

def make_output_path(compiled_root, p):
    return os.path.join(compiled_root, p)


def make_absolute_static_path(static_path, p):
    base = os.path.normpath(os.path.abspath(static_path))
    return os.path.normpath(os.path.join(base, p))


def make_relative_static_path(static_path, p):
    base = os.path.normpath(static_path)
    assert p.startswith(base)
    return p[len(base)+1:]

def _utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf8')
    assert isinstance(s, str)
    return s
