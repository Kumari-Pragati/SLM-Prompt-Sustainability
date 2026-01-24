import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):

    def test_with_positive_numbers(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_with_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3, -4, -5]), -15)

    def test_with_mixed_numbers(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 3)

    def test_with_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_with_single_number(self):
        self.assertEqual(count([5]), 5)
