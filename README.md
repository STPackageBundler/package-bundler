# Sublime Text 2 - Package Bundler

This package allows you to have multiple package sets.

When you're doing some PHP, you don't need Ruby packages.

With this package, you can create multiple presets of "ignored_packages" that you can load at will.

## Installation

Go to your ST2 Packages dir, then:

```bash
$ git clone git://github.com/chadrien/package-bundler.git "Package Bundler"
```

## Configuration

In ST2, goto : Preferences > Package Settings > Package Bundler > Settings - User

```JSON
{
  "bundles": {
    "With Vintage": {
      "ignored_packages": []
    },
    "Without Vintage": {
      "ignored_packages": [ "Vintage" ]
    }
  }
}
```

## Usage

Open Command Palette > Package Bundler : Load Bundle, then choose your bundle.