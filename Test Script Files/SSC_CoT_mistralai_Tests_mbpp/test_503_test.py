import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4]), [1+2, 2+3])
        self.assertListEqual(add_consecutive_nums([5, 6, 7, 8]), [5+6, 6+7])

    def test_edge_cases(self):
        self.assertListEqual(add_consecutive_nums([1]), [])
        self.assertListEqual(add_consecutive_nums([1, 2]), [1+2])
        self.assertListEqual(add_consecutive_nums([1, 2, 3]), [1+2, 2+3])
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1+2, 2+3, 3+4])

    def test_boundary_cases(self):
        self.assertListEqual(add_consecutive_nums([0, 1]), [0])
        self.assertListEqual(add_consecutive_nums([-1, 0]), [-1])
        self.assertListEqual(add_consecutive_nums([-1, 0, 1]), [-1, 0])
        self.assertListEqual(add_consecutive_nums([-1, 0, 1, 2]), [-1, 0, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums(1.234)
        with self.assertRaises(TypeError):
            add_consecutive_nums(['a', 'b', 'c'])
