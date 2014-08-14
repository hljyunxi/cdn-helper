#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>


try:
    import json
except ImportError:
    import simplejson as json


class Manifest(object):
    def __init__(self):
        self._manifest = self.make_empty_manifest()

    def data(self):
        return self._manifest

    def load(self, file_name):
        try:
            self._manifest = json.load(open(file_name))
        except:
            self._manifest = self.make_empty_manifest()
        return self

    def save_to(self, file_name):
        json.dump(self._manifest, open(file_name, 'w'), indent=2, **kwargs)

    def need_recompile(self, new_manifest):
        def asset_in_sync(asset):
            if asset not in self.assets:
                return False
            if self.assets[asset]['version'] != new_manifest[asset]['version']:
                return False

            return True

        return not all(map(assets_in_sync, newer_manifest.assets))

    @property
    def assets(self):
        return self._manifest['assets']

    def union(self, new_manifest):
        self.assets.update(self.new_manifest.assets)

    def make_empty_manifest(self):
        return {
            'assets': {}
        }
