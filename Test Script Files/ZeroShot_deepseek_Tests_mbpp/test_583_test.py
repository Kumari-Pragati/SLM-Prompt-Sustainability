import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_catalan_number_zero(self):
        self.assertEqual(catalan_number(0), 1)

    def test_catalan_number_one(self):
        self.assertEqual(catalan_number(1), 1)

    def test_catalan_number_two(self):
        self.assertEqual(catalan_number(2), 2)

    def test_catalan_number_three(self):
        self.assertEqual(catalan_number(3), 5)

    def test_catalan_number_four(self):
        self.assertEqual(catalan_number(4), 14)

    def test_catalan_number_negative(self):
        with self.assertRaises(Exception):
            catalan_number(-1)

    def test_catalan_number_large(self):
        with self.assertRaises(RecursionError):
            catalan_number(1000)
