import unittest
from797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_sum_in_range_positive(self):
        self.assertEqual(sum_in_Range(1, 5), 6)
        self.assertEqual(sum_in_Range(6, 10), 20)
        self.assertEqual(sum_in_Range(11, 15), 30)

    def test_sum_in_range_zero(self):
        self.assertEqual(sum_in_Range(0, 0), 0)
        self.assertEqual(sum_in_Range(0, 1), 0)

    def test_sum_in_range_negative(self):
        self.assertEqual(sum_in_Range(-1, 0), 0)
        self.assertEqual(sum_in_Range(-2, -1), 0)
        self.assertEqual(sum_in_Range(-5, -1), 0)

    def test_sum_in_range_large(self):
        self.assertEqual(sum_in_Range(1000001, 1000005), 2500000)

    def test_sum_in_range_invalid_input(self):
        self.assertRaises(TypeError, sum_in_Range, 'a', 5)
        self.assertRaises(TypeError, sum_in_Range, 1, 'a')
        self.assertRaises(ValueError, sum_in_Range, -1, -2)
        self.assertRaises(ValueError, sum_in_Range, 0, -1)
