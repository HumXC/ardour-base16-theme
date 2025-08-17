#!/usr/bin/env python
import sys
import re


def make(yaml_file):
    base16 = []
    name = "theme"

    with open(yaml_file, "r") as f:
        data = f.read()
        for line in data.split("\n"):
            if (
                line.startswith("system:")
                or line.startswith("name:")
                or line.startswith("author:")
                or line.startswith("variant:")
            ):
                if line.startswith("name:"):
                    name = line.split(":")[1].strip().replace('"', "")
                print(line)
                continue

            if line.strip().startswith("base0"):
                match = re.search(r'"(.*?)"', line)
                if match:
                    value = match.group(1)
                    base16.append(value.replace("#", "").lower())
                else:
                    raise Exception(f"Invalid line: {line}")

    from xml.dom import minidom

    dom = minidom.parse("theme.xml")
    dom.documentElement.setAttribute("theme-name", name)
    colors_node = dom.getElementsByTagName("Colors")[0]
    for i in range(len(base16)):
        value = base16[i]
        if len(value) == 6:
            value += "ff"
        new_color = dom.createElement("Color")
        new_color.setAttribute("name", f"base{format(i, '02X')}")
        new_color.setAttribute("value", value)
        colors_node.appendChild(dom.createTextNode("\n    "))
        colors_node.appendChild(new_color)
    colors_node.appendChild(dom.createTextNode("\n  "))
    with open(
        f"{name.lower().replace(' ', '_').replace('-', '_')}-ardour.colors", "w"
    ) as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        dom.documentElement.writexml(f)


def main():
    if len(sys.argv) < 2:
        print("Usage: python make.py <...yaml_file>")
        return
    for yaml_file in sys.argv[1:]:
        make(yaml_file)
        print()


if __name__ == "__main__":
    main()
