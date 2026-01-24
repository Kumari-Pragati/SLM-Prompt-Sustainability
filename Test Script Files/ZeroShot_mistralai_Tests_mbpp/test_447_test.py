import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(cube_nums([]), [])

    def test_single_number(self):
        self.assertListEqual(cube_nums([3]), [27])

    def test_positive_numbers(self):
        self.assertListEqual(cube_nums([1, 2, 3, 4, 5]), [1, 8, 27, 64, 125])

    def test_negative_numbers(self):
        self.assertListEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_mixed_numbers(self):
        self.assertListEqual(cube_nums([1, -2, 3, -4, 5]), [1, 8, 27, 64, 125])
