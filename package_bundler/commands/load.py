import sublime
import sublime_plugin

from .base_window import BaseWindowCommand
from ..bundle_loader import BundleLoader

class PackageBundlerLoadCommand(BaseWindowCommand):
    def chosen_bundle(self, picked):
        if picked == -1:
            return

        bundles = self.get_bundles_list()
        picked  = bundles[picked]

        self.get_bundle(picked)

    def get_bundle(self, name):
        bundle = self.settings.get('bundles')[name]

        BundleLoader.load_bundle(name)

        sublime.status_message('Package Bundler: bundle '+name+' loaded')