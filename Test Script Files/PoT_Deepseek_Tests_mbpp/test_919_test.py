import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_zero_element(self):
        self.assertEqual(multiply_list([]), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(multiply_list([1, -2, 3, -4]), -24)

    def test_large_numbers(self):
        self.assertEqual(multiply_list([10**6, 10**6]), 10**12)

    def test_large_and_small_numbers(self):
        self.assertEqual(multiply_list([10**6, 10**-6]), 1)

    def test_float_numbers(self):
        self.assertAlmostEqual(multiply_list([1.5, 2.5]), 3.75)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            multiply_list([1, '2', 3])
