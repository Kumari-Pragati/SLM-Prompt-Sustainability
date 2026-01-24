import unittest
from mbpp_447_code import cube_nums

class TestCubeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cube_nums([1, 2, 3]), [1, 8, 27])

    def test_single_number(self):
        self.assertEqual(cube_nums([5]), [125])

    def test_negative_numbers(self):
        self.assertEqual(cube_nums([-1, -2, -3]), [-1, -8, -27])

    def test_zero(self):
        self.assertEqual(cube_nums([0]), [0])

    def test_empty_list(self):
        self.assertEqual(cube_nums([]), [])

    def test_large_numbers(self):
        self.assertEqual(cube_nums([100]), [100**3])

    def test_decimal_numbers(self):
        self.assertAlmostEqual(cube_nums([2.5]), [15.625])

    def test_mixed_numbers(self):
        self.assertEqual(cube_nums([1, -2, 3.5]), [1, -8, 42.875])
