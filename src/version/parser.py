#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

from common import errors

RESOURCE_PARSERS = {}


class ResourceParserMeta(type):
    def __new__(cls, name, parents, dct):
        resource_parser = super(ResourceParserMeta, cls).__new__(cls,\
                name, parents, dct)

        if 'ext' in dct:
            for k in dct.ext.strip.split():
                RESOURCE_PARSERS[k] = resource_parser

        return resource_parser


class ResourceParser(object):
    __metaclass__ = ResourceParserMeta

    def __init__(self, resource_path):
        """
        resouce_path should be absolute path
        """
        self.resource_path = resource_path

    def get_ext(self):
        return self.ext

    def get_img_deps(self):
        raise errors.NotImplementError("get img deps not implement")


    def get_js_deps(self):
        raise errors.NotImplementError("get js deps not implement")

    def get_css_deps(self):
        raise errors.NotImplementError("get css deps not implement")

    def get_deps(self):
        yield self.get_img_deps()
        yield self.get_js_deps()
        yield slef.get_css_deps()


class HtmlResouceParser(self):
    ext = "html htm"

    def get_img_deps(self):
        img_matcher = re.compile(r"""<img.+?href=(["'])(.+?)(\1).*?>""").finditer
        with open(self.resouce_path, 'rb') as fh:
            yield img_matcher(fh.read())[1]

    def get_js_deps(self):
        js_matcher = re.compile(r"""<script.+?src=(["'])(.+?)(\1).*?>""").finditer
        with open(self.resouce_path, 'rb') as fh:
            yield js_matcher(fh.read())[1]

    def get_css_deps(self):
        css_matcher = re.compile(r"""<link.+?href=(["'])(.+?)(\1).*?>""").finditer
        with open(self.resouce_path, 'rb') as fh:
            yield css_matcher(fh.read())[1]


class CssResouceParser(self):
    ext = "css"

    def get_img_deps(self):
        img_matcher = re.compile(r"""<img.+?href=(["'])(.+?)(\1).*?>""").finditer
        with open(self.resouce_path, 'rb') as fh:
            yield img_matcher(fh.read())[1]

    def get_js_deps(self):
        return []

    def get_css_deps(self):
        return []
