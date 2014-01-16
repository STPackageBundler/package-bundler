def pb_settings_filename():
    return 'Package Bundler.sublime-settings'

def st_settings_filename():
    if int(sublime.version()) >= 2174:
        return 'Preferences.sublime-settings'
    return 'Global.sublime-settings
