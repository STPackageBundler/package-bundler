import sublime
import sublime_plugin

from ..bundle_loader import BundleLoader

class ProjectLoaderEventListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        try:
            project_settings = view.window().project_data()
        except Exception:
            project_settings = None

        if project_settings is None or not 'settings' in project_settings or not 'pb_load_bundle' in project_settings['settings']:
            return

        if project_settings['settings']['pb_load_bundle'] == BundleLoader.get_loaded_bundle():
            return

        BundleLoader.load_bundle(project_settings['settings']['pb_load_bundle'])