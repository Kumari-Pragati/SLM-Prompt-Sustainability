import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(position_min([1, 2, 3, 2, 1]), [3, 4])

    def test_single_element_list(self):
        self.assertListEqual(position_min([1]), [0])

    def test_empty_list(self):
        self.assertListEqual(position_min([]), [])

    def test_minimum_value(self):
        self.assertListEqual(position_min([-10, -9, -8]), [0, 1])

    def test_maximum_value(self):
        self.assertListEqual(position_min([10, 9, 8]), [2])

    def test_duplicate_min_values(self):
        self.assertListEqual(position_min([1, 2, 2, 1]), [2, 3])

    def test_negative_numbers(self):
        self.assertListEqual(position_min([-1, -2, -3]), [0, 1])

    def test_mixed_numbers(self):
        self.assertListEqual(position_min([1, -2, 3, -4, 5]), [1, 3])
