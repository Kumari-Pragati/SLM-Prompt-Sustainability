import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(cube_nums([]), [])

    def test_single_number(self):
        self.assertListEqual(cube_nums([1]), [1])

    def test_positive_numbers(self):
        self.assertListEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_negative_numbers(self):
        self.assertListEqual(cube_nums([-1, -2, -3]), [1, 8, 27])

    def test_mixed_numbers(self):
        self.assertListEqual(cube_nums([1, -2, 3, -4]), [1, 8, 27, 64])

    def test_floats(self):
        self.assertListEqual(cube_nums([1.5, 2.5]), [3.375, 15.3375])

    def test_large_numbers(self):
        self.assertListEqual(cube_nums([1000, 2000, 3000]), [10000000000, 800000000000, 270000000000000])

    def test_invalid_input(self):
        self.assertRaises(TypeError, cube_nums, ['a', 1.5, (3, 4)])
