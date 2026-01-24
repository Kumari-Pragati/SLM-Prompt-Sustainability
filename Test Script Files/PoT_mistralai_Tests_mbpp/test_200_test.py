import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_max([1, 2, 3, 4]), [2, 3])
        self.assertEqual(position_max([-1, -2, -3, -4]), [3, 0])
        self.assertEqual(position_max([0, 0, 1, 0]), [3])
        self.assertEqual(position_max([10, 9, 8, 7]), [3, 2])

    def test_edge_case_single_element(self):
        self.assertEqual(position_max([1]), [0])
        self.assertEqual(position_max([-1]), [0])

    def test_edge_case_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_edge_case_single_max(self):
        self.assertEqual(position_max([1, 1]), [1])
        self.assertEqual(position_max([-1, -1]), [1])

    def test_corner_case_duplicate_max(self):
        self.assertEqual(position_max([1, 1, 2]), [1, 0])
        self.assertEqual(position_max([-1, -1, -2]), [1, 0])
