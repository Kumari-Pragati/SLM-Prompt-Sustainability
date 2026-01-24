import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_sum_Of_Series_typical(self):
        self.assertEqual(sum_Of_Series(2), 28)

    def test_sum_Of_Series_edge(self):
        self.assertEqual(sum_Of_Series(1), 0)

    def test_sum_Of_Series_edge2(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_sum_Of_Series_edge3(self):
        self.assertEqual(sum_Of_Series(-1), 0)

    def test_sum_Of_Series_edge4(self):
        with self.assertRaises(TypeError):
            sum_Of_Series('a')

    def test_sum_Of_Series_edge5(self):
        with self.assertRaises(TypeError):
            sum_Of_Series([1, 2, 3])

    def test_sum_Of_Series_edge6(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(None)
