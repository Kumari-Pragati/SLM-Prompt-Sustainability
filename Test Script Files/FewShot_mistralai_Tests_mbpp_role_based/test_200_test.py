import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_single_max_value(self):
        self.assertEqual(position_max([1, 2, 1]), [1])

    def test_multiple_max_values(self):
        self.assertEqual(position_max([1, 2, 2, 1]), [1, 2])

    def test_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_list_with_zero(self):
        self.assertEqual(position_max([0, 1, 2]), [1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3]), [0])

    def test_list_with_duplicates(self):
        self.assertEqual(position_max([1, 1, 2, 1]), [0, 2, 3])
