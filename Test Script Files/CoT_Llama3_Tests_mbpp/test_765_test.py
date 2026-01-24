import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(is_polite(1), 2)
        self.assertEqual(is_polite(2), 4)
        self.assertEqual(is_polite(3), 6)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            is_polite(-1)

    def test_zero(self):
        self.assertEqual(is_polite(0), 1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_polite('a')

    def test_edge_cases(self):
        self.assertEqual(is_polite(10**10), 10**10 + 1)
