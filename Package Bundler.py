import sublime
import sublime_plugin

config_file = 'Package Bundler.sublime-settings'

class PackageBundlerLoadCommand(sublime_plugin.WindowCommand):
  def run(self):
    bundles = self.get_bundles_list()

    if not bundles:
      sublime.error_message('Package Bundler Error: No bundle to load')
      return

    self.window.show_quick_panel(bundles, self.chosen)

  def get_bundles_list(self):
    self.settings = sublime.load_settings(config_file)

    bundles = map(lambda bundle:
      bundle[0]
    , self.settings.get('bundles').items())

    return bundles

  def chosen(self, picked):
    if picked == -1:
      return

    bundles = self.get_bundles_list()
    picked  = bundles[picked]

    self.get_bundle(picked)

  def get_bundle(self, name):
    self.settings = sublime.load_settings(config_file)

    bundle = self.settings.get('bundles')[name]

    print(bundle['ignored_packages'])
    if bundle['ignored_packages']:
      self.settings = sublime.load_settings('Preferences.sublime-settings')
      self.settings.set('ignored_packages', bundle['ignored_packages'])
      sublime.save_settings('Preferences.sublime-settings')

    sublime.status_message('Package Bundle: bundle '+name+' loaded')