import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(max_sum([1, 2, 3, 4, 5], 5), 15)
        self.assertAlmostEqual(max_sum([10, 20, 30, 40, 50], 5), 160)

    def test_negative_numbers(self):
        self.assertAlmostEqual(max_sum([-1, -2, -3, -4, -5], 5), -15)
        self.assertAlmostEqual(max_sum([-10, -20, -30, -40, -50], 5), -160)

    def test_empty_array(self):
        self.assertEqual(max_sum([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sum([1], 1), 1)
        self.assertEqual(max_sum([-1], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(max_sum([1], 0), 1)
        self.assertEqual(max_sum([-1], 0), -1)

    def test_negative_and_positive_numbers(self):
        self.assertAlmostEqual(max_sum([1, -2, 3, -4, 5], 5), 12)
        self.assertAlmostEqual(max_sum([-1, 2, -3, 4, -5], 5), -8)

    def test_zero(self):
        self.assertEqual(max_sum([0], 1), 0)
        self.assertEqual(max_sum([0, 0], 2), 0)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            max_sum([1, 2, 3], 4)
        with self.assertRaises(ValueError):
            max_sum([1, 2, 3], -1)
