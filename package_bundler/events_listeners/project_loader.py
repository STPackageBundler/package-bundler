import sublime
import sublime_plugin

from ..bundle_loader import BundleLoader

class ProjectLoaderEventListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        project_settings = view.window().project_data()

        if not project_settings['settings']['pb_load_bundle']:
            return

        if project_settings['settings']['pb_load_bundle'] == BundleLoader.get_loaded_bundle():
            return

        BundleLoader.load_bundle(project_settings['settings']['pb_load_bundle'])