import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(catalan_number(0), 1)

    def test_one(self):
        self.assertEqual(catalan_number(1), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_large_positive_numbers(self):
        self.assertEqual(catalan_number(10), 1027)
        self.assertEqual(catalan_number(20), 1355335013671752600)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, catalan_number, -1)
