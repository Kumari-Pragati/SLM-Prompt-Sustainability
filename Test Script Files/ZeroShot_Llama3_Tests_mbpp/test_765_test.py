import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_is_polite_positive(self):
        self.assertEqual(is_polite(1), 2)

    def test_is_polite_negative(self):
        self.assertEqual(is_polite(-1), 2)

    def test_is_polite_zero(self):
        self.assertEqual(is_polite(0), 1)

    def test_is_polite_non_integer(self):
        self.assertEqual(is_polite(1.5), 2)

    def test_is_polite_large_number(self):
        self.assertEqual(is_polite(1000), 2)

    def test_is_polite_small_number(self):
        self.assertEqual(is_polite(-1000), 2)
