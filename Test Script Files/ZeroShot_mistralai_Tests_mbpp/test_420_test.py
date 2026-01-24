import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_sum_for_one(self):
        self.assertEqual(cube_Sum(1), 8)

    def test_cube_sum_for_two(self):
        self.assertEqual(cube_Sum(2), 80)

    def test_cube_sum_for_three(self):
        self.assertEqual(cube_Sum(3), 288)

    def test_cube_sum_for_four(self):
        self.assertEqual(cube_Sum(4), 768)

    def test_cube_sum_for_five(self):
        self.assertEqual(cube_Sum(5), 1728)

    def test_cube_sum_for_large_number(self):
        self.assertEqual(cube_Sum(100), 10000000000)
