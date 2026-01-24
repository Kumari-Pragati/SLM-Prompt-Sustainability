import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(sum_average(3), (6, 2))
        self.assertTupleEqual(sum_average(5), (15, 3))
        self.assertTupleEqual(sum_average(10), (55, 5.5))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(sum_average(0), (0, float('nan')))
        self.assertTupleEqual(sum_average(1), (1, 1))
        self.assertTupleEqual(sum_average(2), (3, 1.5))

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum_average, 'string')
        self.assertRaises(TypeError, sum_average, -1)
        self.assertRaises(TypeError, sum_average, float('-inf'))
        self.assertRaises(TypeError, sum_average, float('inf'))
