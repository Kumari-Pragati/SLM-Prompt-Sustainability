import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(position_max([5]), [0])

    def test_multiple_elements_list(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])

    def test_list_with_duplicates(self):
        self.assertEqual(position_max([1, 2, 2, 3, 3, 3, 4, 5, 5]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_list_with_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])

    def test_list_with_zero(self):
        self.assertEqual(position_max([0, 1, 2, 3, 4]), [0, 1, 2, 3, 4])
