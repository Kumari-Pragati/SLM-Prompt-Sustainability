import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(count([1, -1, 2, -2]), 0)

    def test_large_numbers(self):
        self.assertEqual(count([1000000, 2000000, 3000000]), 6000000)
