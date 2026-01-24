import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(cube_Sum(3), 225)
        self.assertEqual(cube_Sum(5), 625)
        self.assertEqual(cube_Sum(10), 3025)

    def test_edge_cases(self):
        self.assertEqual(cube_Sum(0), 0)
        self.assertEqual(cube_Sum(1), 9)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            cube_Sum(-1)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            cube_Sum(3.5)

    def test_large_inputs(self):
        self.assertEqual(cube_Sum(100), 338350)
