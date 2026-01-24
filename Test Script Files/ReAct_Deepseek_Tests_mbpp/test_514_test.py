import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_empty_tuple(self):
        self.assertEqual(sum_elements(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -1, 2, -2)), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_elements((1000, 2000, 3000)), 6000)

    def test_float_numbers(self):
        self.assertAlmostEqual(sum_elements((1.5, 2.5, 3.5)), 7.5)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            sum_elements((1, 'a', 2))

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            sum_elements(123)
