import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_average(5), (15, 3.0))

    def test_edge_case_zero(self):
        self.assertRaises(ZeroDivisionError, sum_average, 0)

    def test_edge_case_one(self):
        self.assertEqual(sum_average(1), (1, 1.0))

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            sum_average(-5)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            sum_average(5.5)

    def test_edge_case_large_number(self):
        self.assertEqual(sum_average(1000), (500500, 500.5))

    def test_edge_case_zero_after_non_zero(self):
        self.assertEqual(sum_average(10), (55, 5.5))

    def test_edge_case_non_integer_after_integer(self):
        self.assertEqual(sum_average(5), (15, 3.0))

    def test_edge_case_integer_after_non_integer(self):
        self.assertEqual(sum_average(5.5), (15.75, 3.125))
