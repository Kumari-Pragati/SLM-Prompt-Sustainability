import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum(12, 18), 6)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-12, -18), -6)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum(-12, 18), 6)

    def test_sum_zero(self):
        self.assertEqual(sum(0, 18), 0)

    def test_sum_same_numbers(self):
        self.assertEqual(sum(18, 18), 18)

    def test_sum_large_numbers(self):
        self.assertEqual(sum(10000, 20000), 10000)

    def test_sum_with_float(self):
        self.assertEqual(sum(12.5, 18.5), 6)

    def test_sum_with_string(self):
        with self.assertRaises(TypeError):
            sum("12", 18)

    def test_sum_with_list(self):
        with self.assertRaises(TypeError):
            sum([12, 18], 18)
