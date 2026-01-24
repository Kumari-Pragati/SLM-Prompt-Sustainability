import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_negative_numbers(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_zero(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_single_input(self):
        self.assertEqual(cube_nums([4]), [64])

    def test_empty_list(self):
        self.assertEqual(cube_nums([]), [])

    def test_large_numbers(self):
        self.assertEqual(cube_nums([1000, 2000, 3000]), [10000000000, 800000000000, 270000000000000])
