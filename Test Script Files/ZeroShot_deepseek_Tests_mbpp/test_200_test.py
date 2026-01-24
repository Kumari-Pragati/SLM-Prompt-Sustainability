import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_position_max_single_max(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9]), [8])

    def test_position_max_multiple_max(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 8]), [7, 8])

    def test_position_max_all_same(self):
        self.assertEqual(position_max([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])

    def test_position_max_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_position_max_negative_numbers(self):
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [0])

    def test_position_max_mixed_numbers(self):
        self.assertEqual(position_max([-1, 2, -3, 4, -5]), [3])
