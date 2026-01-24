import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_sum_function(self):
        self.assertEqual(_sum([1, 2, 3]), 6)
        self.assertEqual(_sum([-1, -2, -3]), -6)
        self.assertEqual(_sum([0, 0, 0]), 0)
        self.assertEqual(_sum([-1, 0, 1]), 0)
        self.assertEqual(_sum([-1, -2, 3]), 0)
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_empty_array(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(_sum([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, 2, 3, -4, 5]), 7)
