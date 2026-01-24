import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(position_max([1, 2, 3, 4, 5]), [3, 4])
        self.assertListEqual(position_max([10, 20, 30, 40, 50]), [3, 4])

    def test_edge_input(self):
        self.assertListEqual(position_max([1, 1, 1, 1, 1]), [3, 4])
        self.assertListEqual(position_max([10, 9, 8, 7, 6]), [3, 4])
        self.assertListEqual(position_max([5, 4, 3, 2, 1]), [4, 4])
        self.assertListEqual(position_max([5, 4, 3, 2]), [3, 2])

    def test_boundary_input(self):
        self.assertListEqual(position_max([0, 1, 2, 3, 4]), [4])
        self.assertListEqual(position_max([-1, 0, 1, 2, 3]), [4])
        self.assertListEqual(position_max([1, 2, 3, 4, 5]), [4])
        self.assertListEqual(position_max([5, 4, 3, 2, 1]), [4])

    def test_empty_list(self):
        self.assertListEqual(position_max([]), [])

    def test_single_element(self):
        self.assertListEqual(position_max([1]), [0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            position_max(1.5)
        with self.assertRaises(TypeError):
            position_max(('a', 'b', 'c'))
