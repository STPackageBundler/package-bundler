import sublime
import sublime_plugin

from ..settings import *

class BaseWindowCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.settings = sublime.load_settings(pb_settings_filename())
        bundles = self.define_current_bundle(self.get_bundles_list())

        if len(bundles) == 0:
            sublime.error_message('Package Bundler Error: No bundle to load')
            return

        self.show_quick_panel(bundles, self.chosen_bundle)

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