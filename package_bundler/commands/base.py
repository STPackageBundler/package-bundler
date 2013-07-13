import sublime
import sublime_plugin

from ..settings import settings_filename

class BaseWindowCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.settings = sublime.load_settings(settings_filename())
        bundles = self.get_bundles_list()

        if len(bundles) == 0:
            sublime.error_message('Package Bundler Error: No bundle to load')
            return

        self.window.show_quick_panel(bundles, self.chosen)

    def get_bundles_list(self):
        if not self.settings.get('bundles'):
            return []

        bundles = list(map(lambda bundle:
            bundle[0]
            , self.settings.get('bundles').items()))

        bundles = self.define_current_bundle(bundles)

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

    def chosen(self):
        raise NotImplementedError