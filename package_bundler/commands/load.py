import sublime
import sublime_plugin

from ..settings import settings_filename

class PackageBundlerLoadCommand(sublime_plugin.WindowCommand):
  def run(self):
    bundles = self.get_bundles_list()

    if len(bundles) == 0:
      sublime.error_message('Package Bundler Error: No bundle to load')
      return

    self.window.show_quick_panel(bundles, self.chosen)

  def get_bundles_list(self):
    settings = sublime.load_settings(settings_filename())

    if not settings.get('bundles'):
      return []

    bundles = list(map(lambda bundle:
      bundle[0]
    , settings.get('bundles').items()))

    return bundles

  def chosen(self, picked):
    if picked == -1:
      return

    bundles = self.get_bundles_list()
    picked  = bundles[picked]

    self.get_bundle(picked)

  def get_bundle(self, name):

    bundle = self.settings.get('bundles')[name]

    self.write_ignored_packages(bundle)

    sublime.status_message('Package Bundle: bundle '+name+' loaded')

  def write_ignored_packages(self, bundle):
    settings = sublime.load_settings(settings_filename())

    if bundle['ignored_packages']:
      settings = sublime.load_settings('Preferences.sublime-settings')
      settings.set('ignored_packages', bundle['ignored_packages'])
      sublime.save_settings('Preferences.sublime-settings')