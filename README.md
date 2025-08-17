# **Ardour Base16 Theme**

English | [简体中文](README_zh-CN.md)

A simple script to import base16 color schemes into Ardour audio workstation.

## Usage

You can preview the color schemes from <https://tinted-theming.github.io/tinted-gallery/> and download the corresponding `.yaml` files from <https://github.com/chriskempson/base16>.

Then run `make.py <xxx1.yaml> <xxx2.yaml>` command, which will generate the corresponding `xxx-ardour.colors` file in the directory. Copy this file to the `themes` folder in the Ardour configuration directory, and the theme will be available the next time you start Ardour and select it from `preference -> colors`.

You can also install base16 color schemes from your Linux distribution's package manager, such as in nix, you can use `nix build nixpkgs#base16-schemes` to get the color schemes.
