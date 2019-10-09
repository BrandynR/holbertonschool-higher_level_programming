#!/usr/bin/python3
"""Function to format text."""


def text_indentation(text):
    """Will format input text by adding \n.
    Searches through input string and will add two newlines
        after the characters '.', '?', and ':'.
    Args:
        text (str): input text to be formatted.
    Raises:
        TypeError: if input is not a string
    """

    form = ['.', '?', ':']
    start = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i, x in enumerate(text):
        if x in form:
            print(text[start:i + 1].strip() + '\n')
            start = i + 1
    print(text[start:].strip(), end='')
