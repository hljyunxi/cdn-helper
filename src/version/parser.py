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

    def get_img_deps(content, self):
        raise errors.NotImplementError("get img deps not implement")


    def get_js_deps(content, self):
        raise errors.NotImplementError("get js deps not implement")

    def get_css_deps(content, self):
        raise errors.NotImplementError("get css deps not implement")

    def get_deps(self):
        with open(self.resouce_path, 'rb') as fh:
            file_content = fh.read()
            yield self.get_img_deps(file_content)
            yield self.get_js_deps(file_content)
            yield slef.get_css_deps(file_content)


class HtmlResouceParser(self):
    ext = ".html .htm"

    def get_img_deps(self, file_content):
        img_matcher = re.compile(r"""<img.+?href=(["'])(.+?)(\1).*?>""").finditer
        yield img_matcher(file_content)

    def get_js_deps(self, file_content):
        js_matcher = re.compile(r"""<script.+?src=(["'])(.+?)(\1).*?>""").finditer
        yield js_matcher(file_content)

    def get_css_deps(self, file_content):
        css_matcher = re.compile(r"""<link.+?href=(["'])(.+?)(\1).*?>""").finditer
        yield css_matcher(file_content)


class CssResouceParser(self):
    ext = ".css"

    def get_img_deps(self, file_content):
        img_matcher = re.compile(r"""<img.+?src=(["'])(.+?)(\1).*?>""").finditer
        yield img_matcher(file_content)

    def get_js_deps(self):
        return []

    def get_css_deps(self):
        return []
