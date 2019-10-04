#!/usr/bin/python3
"""
text_indentation:
 module that indents text
"""


def text_indentation(text):
    """
    text_indentation: formats text
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    string = ""
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
