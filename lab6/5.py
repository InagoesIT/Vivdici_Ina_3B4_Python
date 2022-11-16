# Write another variant of the function from the previous exercise that
# returns those elements that have at least one attribute that corresponds
# to a key-value pair in the dictionary.

import re
from lxml import etree


def get_attr_and_tag_expr(attrs: dict):
    attr_expression = ""
    for key, value in attrs.items():
        attr_expression += f'{key}="{value}"|'
    return re.compile(f'\\s*<.+ ({attr_expression[:-1]}).*>'), re.compile(r"\s<(?P<tag_name>\w+)\s.*>")


def get_element(tag_name: str, lines: list, i: int) -> (str, int):
    tag_end_expr = re.compile(f"</{tag_name}>")
    element = ""
    lines_nr = len(lines)

    while i < lines_nr and tag_end_expr.search(lines[i]) is None:
        element += lines[i]
        i += 1
    element += lines[i]

    return element


def get_elements_with_attrs(xml_path: str, attrs: dict) -> list:
    file = open(xml_path, "r")
    elements = list()
    attr_expression, tag_name_expr = get_attr_and_tag_expr(attrs)

    lines = file.readlines()
    i = 0
    lines_nr = len(lines)
    while i < lines_nr:
        line = lines[i]
        if attr_expression.match(line) is None:
            i += 1
            continue
        tag_name = tag_name_expr.search(line).group("tag_name")
        element = get_element(tag_name, lines, i)
        elements.append(element)
        i += 1

    file.close()

    return elements


if __name__ == '__main__':
    attrs_dict = {"category": "children", "theme": "wow", "rating": "big"}
    path = "book.xml"
    elements_str = get_elements_with_attrs(path, attrs_dict)

    for element_str in elements_str:
        root = etree.fromstring(element_str)
        print(etree.tostring(root, pretty_print=True).decode())
