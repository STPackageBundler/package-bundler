import sublime
import sublime_plugin

from ..settings import *
from .base import BaseWindowCommand

class PackageBundlerLoadCommand(BaseWindowCommand):
    def chosen_bundle(self, picked):
        if picked == -1:
            return

        bundles = self.get_bundles_list()
        picked  = bundles[picked]

        self.get_bundle(picked)

    def get_bundle(self, name):
        bundle = self.settings.get('bundles')[name]

        self.write_ignored_packages(bundle)
        self.save_loaded_package(name)

        sublime.status_message('Package Bundle: bundle '+name+' loaded')

    def write_ignored_packages(self, bundle):    
        if bundle['ignored_packages']:
            settings = sublime.load_settings(st_settings_filename())
            settings.set('ignored_packages', bundle['ignored_packages'])
            sublime.save_settings(st_settings_filename())

    def save_loaded_package(self, name):
        self.settings.set('loaded_bundle', name)
        sublime.save_settings(pb_settings_filename())