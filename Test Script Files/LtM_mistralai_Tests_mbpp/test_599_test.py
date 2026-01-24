import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_average(1), (1, 1))
        self.assertEqual(sum_average(2), (3, 1.5))
        self.assertEqual(sum_average(3), (6, 2))

    def test_edge_input(self):
        self.assertEqual(sum_average(0), (0, None))
        self.assertEqual(sum_average(100000), (5000050, 50))

    def test_negative_input(self):
        self.assertRaises(ValueError, sum_average, -1)
