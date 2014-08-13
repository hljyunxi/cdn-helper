#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import sys

class Builder(object):
    def __init__(self, setting):
        self.setting = setting

    def get_files(self, paths, exts):
        pass

    def build_manifest(self, files):
        pass

    def need_recomiple(self, old_manifest, current_manifest):
        pass

    def get_reverse_deps(self, manifest, files):
        pass

    def write_versioned_files(self, reverse_deps_map):
        pass

    def write_manifest(self, manifest):
        pass
