import sublime

from .base_window import BaseWindowCommand
from ..settings import *

class PackageBundlerCreateBundleCommand(BaseWindowCommand):
    def run(self):
        self.settings = sublime.load_settings(pb_settings_filename())
        
        self.window.show_input_panel('Bundle name:', '', self.create_bundle, None, None)

    def create_bundle(self, bundle_name):
        bundles = self.settings.get('bundles')

        if bundles is None:
            bundles = {}

        bundles[bundle_name] = {"ignored_packages": []}

        self.settings.set('bundles', bundles)
        sublime.save_settings(pb_settings_filename())
        sublime.status_message('Bundle created!')
