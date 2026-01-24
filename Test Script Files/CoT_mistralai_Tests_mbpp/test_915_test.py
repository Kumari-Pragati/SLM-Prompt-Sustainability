import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_zero(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_positive_numbers(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(rearrange_numbs([0, 1, -2, 3, -4, 5, -6]), [1, -2, 3, -4, 5, -6, 0])

    def test_floats(self):
        self.assertListEqual(rearrange_numbs([0.1, 0.2, 0.3, 0.4, 0.5]), [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_large_numbers(self):
        self.assertListEqual(rearrange_numbs([1000000000, 999999999, 1, 0, -1]), [1, 0, -1, 999999999, 1000000000])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearrange_numbs('not a number')
