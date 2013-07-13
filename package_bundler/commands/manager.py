import sublime
import sublime_plugin

from ..settings import *
from .base import BaseWindowCommand

PackageControl = __import__('Package Control')

class PackageBundlerManagerCommand(BaseWindowCommand):
    management_options_label = ['Add ignored package', 'Remove ignored package']

    def chosen_bundle(self, picked):
        if picked == -1:
            return

        bundles = self.get_bundles_list()
        self.picked_bundle = bundles[picked]

        self.show_quick_panel(self.management_options_label, self.chosen_management)

    def chosen_management(self, picked):
        if picked == -1:
            return

        packages_list = self.get_ignorable_packages()

        if not packages_list:
            sublime.error_message('There is not package to disable')
            return

        self.show_quick_panel(
            packages_list,
            lambda package:
                self.management_options[picked](self, package)
        )

    def add_ignored_package(self, picked):
        if picked == -1:
            return

        packages_list = self.get_ignorable_packages()
        ignored_package = packages_list[picked]
        bundles = self.settings.get('bundles')

        bundle_ignored_packages = bundles[self.picked_bundle]['ignored_packages']
        bundle_ignored_packages.append(ignored_package)
        bundle_ignored_packages.sort()

        self.settings.set('bundles', bundles)
        sublime.save_settings(pb_settings_filename())

        sublime.status_message('Package Bundle: package '+ignored_packages+' added to '+self.picked_bundle+' bundle\'s ignore list')

    def remove_ignored_package(self):
        print('remove')

    def get_ignorable_packages(self):
        manager = PackageControl.package_control.package_manager.PackageManager()

        all_packages = manager.list_all_packages()
        ignored_packages = self.settings.get('bundles')[self.picked_bundle]['ignored_packages']

        if not ignored_packages:
            ignored_packages = []

        packages_list = list(set(all_packages) - set(ignored_packages))
        packages_list.sort()

        return packages_list

    management_options = {
        0: add_ignored_package,
        1: remove_ignored_package
    }