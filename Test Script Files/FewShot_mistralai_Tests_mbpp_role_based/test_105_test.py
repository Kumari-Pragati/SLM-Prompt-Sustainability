import unittest
from mbpp_105_code import count

class TestCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 6)

    def test_duplicate_numbers(self):
        self.assertEqual(count([1, 1, 2, 3]), 6)

    def test_large_list(self):
        self.assertEqual(count(list(range(1000))), 499900)
