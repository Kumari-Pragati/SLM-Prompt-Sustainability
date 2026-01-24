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

    def test_zero(self):
        self.assertListEqual(cube_nums([0]), [0])

    def test_floats(self):
        self.assertAlmostEqual(cube_nums([1.5]), [1.3312076908403935], delta=0.01)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            cube_nums([1, "two", 3])
