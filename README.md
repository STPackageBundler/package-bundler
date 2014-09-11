# Sublime Text 3 - Package Bundler

This package allows you to have multiple package sets.

When you're doing some PHP, you don't need Ruby packages.

With this package, you can create multiple presets of "ignored_packages" that you can load at will.

## Sublime Text 2 compatibility

For a recent development I had to do for issue #2, I used features avalaible from ST3 only.

As ST3 is now in public beta and should soon be released as stable, I don't want to "waste" time maintaining this package for a "soon-to-be-outdated" version.

If many people ask me to be compatible again with ST2, I'll manage to do it.

## Installation

### Package Control (mandatory)

Search "Package Bundler" into Package Control

Installation through Package Control is mandatory because Package Bundler uses Package Control classes.

## Usage

### Load a bundle

Open Command Palette > Package Bundler: Load Bundle, then choose your bundle.

### Add and ignored package to a bundle

Open Command Palette > Package Bundler: Manage Bundle

### Create a bundle

Open Command Palette > Package Bundler: Create Bundle

### Auto load a bundle per project

You can open your _project_.sublime-settings and add a setting to auto load a bundle for this project.

```json
{
    "folders":
    [
        {
            "follow_symlinks": true,
            "path": "/path/to/project"
        }
    ],
    "settings":
    {
        "pb_load_bundle": "YourBundle"
    }
}
```
