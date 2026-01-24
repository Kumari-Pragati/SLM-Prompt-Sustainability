import unittest
from mbpp_798_code import _sum

class TestSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3]), -6)

    def test_single_number(self):
        self.assertEqual(_sum([7]), 7)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 4)
