import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_zero_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_negative_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], -2), [-2, -4, -6])

    def test_empty_list(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_large_numbers(self):
        self.assertEqual(ntimes_list([1000000, 2000000], 2), [2000000, 4000000])

    def test_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_decimal_numbers(self):
        self.assertEqual(ntimes_list([1.5, 2.5, 3.5], 2), [3.0, 5.0, 7.0])

    def test_string_input(self):
        with self.assertRaises(TypeError):
            ntimes_list(['1', '2', '3'], 2)

    def test_non_integer_multiplier(self):
        with self.assertRaises(TypeError):
            ntimes_list([1, 2, 3], 2.5)
