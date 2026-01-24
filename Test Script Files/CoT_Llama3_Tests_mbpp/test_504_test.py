import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_sum_of_series(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 28)
        self.assertEqual(sum_Of_Series(3), 109)
        self.assertEqual(sum_Of_Series(4), 216)
        self.assertEqual(sum_Of_Series(5), 377)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(-1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Of_Series('a')
