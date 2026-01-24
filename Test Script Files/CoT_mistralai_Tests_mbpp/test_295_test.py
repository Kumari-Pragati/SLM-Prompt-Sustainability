import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_div(4), 3)
        self.assertEqual(sum_div(6), 3)
        self.assertEqual(sum_div(28), 14)
        self.assertEqual(sum_div(496), 712)

    def test_zero_and_one(self):
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(1), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_div(-4), 4)
        self.assertEqual(sum_div(-21), 4)
        self.assertEqual(sum_div(-20), 4)

    def test_edge_cases(self):
        self.assertEqual(sum_div(2), 1)
        self.assertEqual(sum_div(3), 1)
        self.assertEqual(sum_div(5), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_div, 'string')
        self.assertRaises(TypeError, sum_div, -1.5)
        self.assertRaises(TypeError, sum_div, complex(1, 2))
