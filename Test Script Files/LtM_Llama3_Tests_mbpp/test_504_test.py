import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 28)
        self.assertEqual(sum_Of_Series(3), 109)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(-1), 0)
        self.assertEqual(sum_Of_Series(100), 33325000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Of_Series('a')
        with self.assertRaises(TypeError):
            sum_Of_Series(None)
