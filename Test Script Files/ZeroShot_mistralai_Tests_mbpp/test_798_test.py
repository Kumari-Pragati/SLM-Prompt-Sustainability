import unittest
from798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(_sum([1]), 1)

    def test_positive_numbers_list(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers_list(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), 15)

    def test_mixed_numbers_list(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 6)
