import unittest
from mbpp_765_code import math
from765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_is_polite_positive_numbers(self):
        self.assertEqual(is_polite(1), 2)
        self.assertEqual(is_polite(2), 3)
        self.assertEqual(is_polite(3), 5)
        self.assertEqual(is_polite(4), 7)
        self.assertEqual(is_polite(5), 11)
        self.assertEqual(is_polite(6), 13)
        self.assertEqual(is_polite(7), 17)
        self.assertEqual(is_polite(8), 19)
        self.assertEqual(is_polite(9), 23)
        self.assertEqual(is_polite(10), 29)

    def test_is_polite_zero(self):
        self.assertNotEqual(is_polite(0), 1)

    def test_is_polite_negative_numbers(self):
        self.assertNotEqual(is_polite(-1), 0)
        self.assertNotEqual(is_polite(-2), 1)
        self.assertNotEqual(is_polite(-3), 2)
        self.assertNotEqual(is_polite(-4), 3)
        self.assertNotEqual(is_polite(-5), 4)
        self.assertNotEqual(is_polite(-6), 5)
        self.assertNotEqual(is_polite(-7), 6)
        self.assertNotEqual(is_polite(-8), 7)
        self.assertNotEqual(is_polite(-9), 8)
        self.assertNotEqual(is_polite(-10), 9)
