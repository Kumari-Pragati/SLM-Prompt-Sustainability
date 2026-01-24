import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_sum_elements_typical(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_sum_elements_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_sum_elements_single_element(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_sum_elements_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_sum_elements_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3, -4)), -2)

    def test_sum_elements_non_integer(self):
        with self.assertRaises(TypeError):
            sum_elements((1, 2, 'a'))
