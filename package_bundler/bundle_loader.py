import sublime
from .settings import *

class BundleLoader:
    def load_bundle(bundle_name):
        BundleLoader.load_settings()

        BundleLoader.write_ignored_packages(bundle_name)
        BundleLoader.save_loaded_package(bundle_name)

    def load_settings():
        BundleLoader.settings = sublime.load_settings(pb_settings_filename())

    def write_ignored_packages(bundle_name):
        bundle = BundleLoader.settings.get('bundles')[bundle_name]

        if bundle['ignored_packages']:
            settings = sublime.load_settings(st_settings_filename())
            settings.set('ignored_packages', bundle['ignored_packages'])
            sublime.save_settings(st_settings_filename())

    def save_loaded_package(bundle_name):
        BundleLoader.settings.set('loaded_bundle', bundle_name)
        sublime.save_settings(pb_settings_filename())

    def get_loaded_bundle():
        BundleLoader.load_settings()

        return BundleLoader.settings.get('loaded_bundle')