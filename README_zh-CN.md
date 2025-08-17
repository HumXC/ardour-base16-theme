# **Ardour Base16 Theme**

[English](README.md) | 中文

一个简单的脚本，用于将 base16 配色方案导入 Ardour 音频工作站。

## 使用

你可以从 <https://tinted-theming.github.io/tinted-gallery/> 预览配色 然后在 <https://github.com/chriskempson/base16> 仓库中下载对应的 .yaml 文件。

然后运行 `make.py <xxx1.yaml> <xxx2.yaml>` 命令，会在目录下生成 对应的 `xxx-ardour.colors` 文件。 将这个文件复制到 ardour 配置文件夹中的 themes 文件夹下，便能在下一次启动 Ardour后在 `preference -> colors` 中选择该主题

你也可以从你所使用的linux发行版的包管理器安装 base16 的color schemes, 例如在 nix 上，可以使用 `nix build nixpkgs#base16-schemes` 获取配色方案。
