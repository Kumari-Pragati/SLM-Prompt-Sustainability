import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_empty_tuple(self):
        self.assertEqual(sum_elements(()), 0)

    def test_single_element(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_mixed_signs(self):
        self.assertEqual(sum_elements((-1, 2, 3)), 4)

    def test_large_numbers(self):
        self.assertEqual(sum_elements((100, 200, 300)), 600)

    def test_non_integer_numbers(self):
        self.assertEqual(sum_elements((1.5, 2.5, 3.5)), 7.5)
