#!/usr/bin/python3
""" unit tests for square """
import unittest
import pep8
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Class rectangle tests """
    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
def test_hack(self):
        self.assertEqual(Base.__doc__, "Test")
