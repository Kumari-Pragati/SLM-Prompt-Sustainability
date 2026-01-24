import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_cube_sum_for_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_cube_sum_for_one(self):
        self.assertEqual(cube_Sum(1), 1)

    def test_cube_sum_for_small_numbers(self):
        self.assertEqual(cube_Sum(2), 9)
        self.assertEqual(cube_Sum(3), 36)
        self.assertEqual(cube_Sum(4), 100)

    def test_cube_sum_for_large_numbers(self):
        self.assertEqual(cube_Sum(10), 2200)
        self.assertEqual(cube_Sum(100), 30422400)
        self.assertEqual(cube_Sum(1000), 30424368000)
