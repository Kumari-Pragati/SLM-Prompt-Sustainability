import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_max([1]), [0])

    def test_multiple_elements_list(self):
        self.assertEqual(position_max([1, 2, 1, 3, 2, 1]), [3, 0, 1])

    def test_duplicate_max_values(self):
        self.assertEqual(position_max([1, 2, 3, 2, 3, 2]), [4, 1, 2])

    def test_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3]), [0, 1, 2])

    def test_mixed_numbers(self):
        self.assertEqual(position_max([1, -2, 3, -4, 5]), [2, 3, 0, 4])
