import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(position_min([1, 2, 3, 1, 2, 3]), [0, 3, 4])
        self.assertListEqual(position_min([-1, -2, -3, -1, -2, -3]), [0, 3, 4])
        self.assertListEqual(position_min([0, 0, 0]), [0, 1, 2])

    def test_edge_cases(self):
        self.assertListEqual(position_min([1]), [0])
        self.assertListEqual(position_min([1, 1]), [0])
        self.assertListEqual(position_min([1, 2, 1]), [1, 0])
        self.assertListEqual(position_min([1, 2, 3, 1]), [3, 0])
        self.assertListEqual(position_min([1, 2, 3, 1, 2]), [4, 0])
        self.assertListEqual(position_min([1, 2, 3, 1, 2, 3]), [4, 0, 5])

    def test_empty_list(self):
        self.assertListEqual(position_min([]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            position_min(123)
        with self.assertRaises(TypeError):
            position_min(None)
