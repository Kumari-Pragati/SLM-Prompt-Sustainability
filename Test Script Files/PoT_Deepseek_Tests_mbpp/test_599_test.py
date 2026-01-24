import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_average(5), (15, 3))

    def test_edge_case_with_zero(self):
        self.assertEqual(sum_average(0), (0, 0))

    def test_boundary_case_with_one(self):
        self.assertEqual(sum_average(1), (1, 1))

    def test_corner_case_with_max_int(self):
        self.assertEqual(sum_average(2**31 - 1), ((2**31 - 1) * (2**31) // 2, (2**31 - 1) * (2**31) // 2 // (2**31 - 1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_average('five')
