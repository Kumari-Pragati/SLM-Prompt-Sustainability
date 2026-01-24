import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_single_element(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((-1, 2, -3)), -2)

    def test_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3, -4)), -2)

    def test_large_numbers(self):
        self.assertEqual(sum_elements((100, 200, 300)), 600)

    def test_float_numbers(self):
        self.assertEqual(sum_elements((1.0, 2.0, 3.0)), 6.0)
