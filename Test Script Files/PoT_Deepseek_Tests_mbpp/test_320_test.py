import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 4)
        self.assertEqual(sum_difference(3), 22)

    def test_edge_cases(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(1), 0)

    def test_boundary_cases(self):
        self.assertEqual(sum_difference(10), 2640)
        self.assertEqual(sum_difference(100), 25164150)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_difference('a')
        with self.assertRaises(TypeError):
            sum_difference(None)
        with self.assertRaises(TypeError):
            sum_difference([])
