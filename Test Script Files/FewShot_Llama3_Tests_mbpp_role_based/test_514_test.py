import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_sum_of_positive_numbers(self):
        self.assertEqual(sum_elements((1, 2, 3, 4, 5)), 15)

    def test_sum_of_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3, -4, -5)), -15)

    def test_sum_of_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3, -4, 5)), 3)

    def test_sum_of_zero(self):
        self.assertEqual(sum_elements(()), 0)

    def test_sum_of_single_element(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_sum_of_empty_tuple(self):
        with self.assertRaises(TypeError):
            sum_elements(())
