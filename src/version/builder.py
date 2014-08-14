#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import sys

class Builder(object):
    def __init__(self, setting):
        assert(all([ i in setting for i in (
            'output_path',
            'static_path',
            'manifest_path',
        )])), "setting error"

        self.setting = setting

    def get_files(self, paths, exts):
        pass

    @property
    def empty_manifest_entry(self):
        return {'version': None, 'deps': []}

    def build_manifest_deps(self, src_files):
        assert isinstance(src_files, (list, tuple)), src_files

        travelled_files = set()
        manifest = Manifest()

        def _build_manifest_helper(src_files, manifest, travelled_files):
            for src_file in src_files:
                rel_src_file = utils.make_relative_path(self.setting.static_path,\
                        src_file)
                manifest.assets.setdefault(rel_src_file, self.emptry_manifest_entry)
                travelled_files.add(src_file)

                for dep_file in IterTools(self.setting.static_path)\
                        .get_deps(src_file):
                    rel_dep_file = utils.make_relative_path(dep_file)
                    manifest.assets[rel_sr_file].append(rel_dep_file)
                    if dep_file not in travelled_file and dep_file in:
                        _build_manifest_helper([dep_file], manifest, travelled_files)

        _build_manifest_helper(src_files, manifest, travelled_files)
        return manifest


    def merge_manifest(self, old_manifest, current_manifest):
        ret_manifest = copy.deepcopy(old_manifest)
        if old_manifest.need_recompile(current_manifest)
            old_manifest.union(current_manifest)

        return ret_manifest

    def get_reverse_deps(self, manifest, files):
        ret = {}
        for k, v in manifest.assets:
            for i in v.deps if i in files:
                ret.setdefault(k, []).append((i, manifest.assets[i].version))

    def write_versioned_files(self, reverse_deps_map):
        for k, v in reverse_deps_map.iteritems():
            abs_file = utils.make_absolute_path(self.setting.static_path, k)
            file_content = open(abs_file).read()
            for path, version in v:
                file_content = re.sub(r"""(['"])(%s)(?:\?.+?)?(\1)"""%path,\
                        r'\2?%s'% version, file_content)
            with open(utils.make_absolute_path(self.setting.output_path, k))\
                    as wfh:
                wfh.write(file_content)

    def write_manifest(self, manifest):
        manifest.save_to(utils.make_absolute_path(self.setting.manifest_path))
