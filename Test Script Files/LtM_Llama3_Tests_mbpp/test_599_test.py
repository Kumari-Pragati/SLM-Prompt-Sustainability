import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_average(1), (1, 1.0))
        self.assertEqual(sum_average(2), (3, 1.5))
        self.assertEqual(sum_average(3), (6, 2.0))
        self.assertEqual(sum_average(4), (10, 2.5))
        self.assertEqual(sum_average(5), (15, 3.0))

    def test_edge(self):
        self.assertEqual(sum_average(0), (0, 0.0))
        self.assertEqual(sum_average(1), (1, 1.0))
        self.assertEqual(sum_average(10), (55, 5.5))
        self.assertEqual(sum_average(100), (5050, 50.5))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum_average('a')
        with self.assertRaises(TypeError):
            sum_average(None)
