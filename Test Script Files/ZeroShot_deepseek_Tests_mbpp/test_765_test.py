import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(10), 12)
        self.assertEqual(is_polite(100), 104)

    def test_zero(self):
        self.assertEqual(is_polite(0), 2)

    def test_negative_numbers(self):
        self.assertEqual(is_polite(-1), 2)
        self.assertEqual(is_polite(-10), 2)

    def test_large_numbers(self):
        self.assertEqual(is_polite(1000), 1004)
        self.assertEqual(is_polite(10000), 10004)
