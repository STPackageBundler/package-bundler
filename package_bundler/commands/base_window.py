import sublime
import sublime_plugin

from ..settings import *

class BaseWindowCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.settings = sublime.load_settings(pb_settings_filename())
        bundles = self.define_current_bundle(self.get_bundles_list())

        if len(bundles) == 0:
            sublime.error_message("Package Bundler: No bundle to load.\nPlease enter a first bundle name.")
            self.window.show_input_panel('Bundle name:', '', self.create_first_bundle, None, None)
            return

        self.show_quick_panel(bundles, self.chosen_bundle)

    def create_first_bundle(self, bundle_name):
        self.settings.set('bundles', {bundle_name: {"ignored_packages": []}})
        sublime.save_ettings(pb_settings_filename())
        sublime.status_message('Bundle created!')

    def get_bundles_list(self):
        if not self.settings.get('bundles'):
            return []

        bundles = list(map(lambda bundle:
            bundle[0]
            , self.settings.get('bundles').items()))

        return bundles

    def define_current_bundle(self, bundles):
        loaded_bundle = self.settings.get('loaded_bundle')

        if not loaded_bundle:
            return bundles

        for i in range(len(bundles)):
            if bundles[i] == loaded_bundle:
                bundles[i] += ' (Current)'
                break

        return bundles

    def chosen_bundle(self):
        raise NotImplementedError

    def show_quick_panel(self, options, done):
        sublime.set_timeout(lambda: self.window.show_quick_panel(options, done), 10)