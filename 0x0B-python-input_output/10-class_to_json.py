#!/usr/bin/python3
"""enter class attributes and values into a dict."""


def class_to_json(obj):
    """Return dict of class fields and values."""
    return obj.__dict__
