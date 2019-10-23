#!/usr/bin/python3
""" Unit testing for base """
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """ Class for testing base """
    def test_value(self):
        """ Tests value of Base """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_value_increment(self):
        """ Tests incrementing """
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_value_set(self):
        """ Tests setting """
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_value_increment2(self):
        """ Tests incrementing after setting """
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
