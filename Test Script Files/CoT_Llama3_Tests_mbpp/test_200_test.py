import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_position_max_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_position_max_single_element_list(self):
        self.assertEqual(position_max([1]), [0])

    def test_position_max_multiple_elements_list(self):
        self.assertEqual(position_max([1, 2, 3, 2, 1]), [0, 4])

    def test_position_max_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3, -2, -1]), [0, 4])

    def test_position_max_duplicates(self):
        self.assertEqual(position_max([1, 2, 2, 3, 1]), [0, 2, 4])

    def test_position_max_duplicates_and_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -2, -3, -1]), [0, 3, 4])

    def test_position_max_empty_list_with_duplicates(self):
        self.assertEqual(position_max([1, 1, 1]), [0, 1, 2])

    def test_position_max_single_element_list_with_duplicates(self):
        self.assertEqual(position_max([1, 1, 1, 1]), [0, 1, 2, 3])
