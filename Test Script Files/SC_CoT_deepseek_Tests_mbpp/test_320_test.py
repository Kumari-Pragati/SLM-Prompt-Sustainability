import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_difference(5), 110)

    def test_boundary_case(self):
        self.assertEqual(sum_difference(1), 0)

    def test_edge_case(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(-1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_difference('a')
