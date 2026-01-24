import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(position_max([1, 2, 3]), [2, 4])
        self.assertListEqual(position_max([-1, -2, -3]), [0, 2])
        self.assertListEqual(position_max([0, 0, 0]), [0, 1, 2])

    def test_edge_cases(self):
        self.assertListEqual(position_max([1]), [0])
        self.assertListEqual(position_max([1, 1]), [1])
        self.assertListEqual(position_max([1, 2, 1]), [1, 2])
        self.assertListEqual(position_max([1, 2, 3, 1]), [2, 4])
        self.assertListEqual(position_max([1, 2, 3, 1, 2]), [3, 4])
        self.assertListEqual(position_max([1, 2, 3, 1, 2, 1]), [3, 4, 5])
        self.assertListEqual(position_max([1, 1, 1]), [0, 1, 2])
        self.assertListEqual(position_max([-1, -1, -1]), [0, 1, 2])

    def test_empty_list(self):
        self.assertListEqual(position_max([]), [])

    def test_single_value_list(self):
        self.assertListEqual(position_max([1]), [0])
        self.assertListEqual(position_max([-1]), [0])
