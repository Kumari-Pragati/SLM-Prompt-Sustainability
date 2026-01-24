import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_first(self):
        self.assertEqual(find_lucas(1), 1)

    def test_typical_cases(self):
        self.assertEqual(find_lucas(5), 11)
        self.assertEqual(find_lucas(10), 123)

    def test_negative_numbers(self):
        with self.assertRaises(Exception):
            find_lucas(-1)

    def test_large_numbers(self):
        with self.assertRaises(RecursionError):
            find_lucas(1000)
