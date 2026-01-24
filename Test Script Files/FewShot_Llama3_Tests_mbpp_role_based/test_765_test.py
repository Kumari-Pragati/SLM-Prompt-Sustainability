import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(is_polite(1), 2)

    def test_negative_numbers(self):
        self.assertEqual(is_polite(-1), 2)

    def test_zero(self):
        self.assertEqual(is_polite(0), 1)

    def test_large_numbers(self):
        self.assertEqual(is_polite(100), 105)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            is_polite(1.5)
