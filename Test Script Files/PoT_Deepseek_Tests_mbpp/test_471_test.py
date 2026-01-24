import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_remainder([10, 20, 30], 3, 100), 0)

    def test_edge_case_with_single_element(self):
        self.assertEqual(find_remainder([5], 1, 7), 5)

    def test_boundary_case_with_large_numbers(self):
        self.assertEqual(find_remainder([10**10, 20**10, 30**10], 3, 10**10), 0)

    def test_invalid_input_with_negative_numbers(self):
        with self.assertRaises(Exception):
            find_remainder([-1, -2, -3], 3, 10)

    def test_invalid_input_with_zero_length_array(self):
        with self.assertRaises(Exception):
            find_remainder([], 0, 10)

    def test_invalid_input_with_negative_n(self):
        with self.assertRaises(Exception):
            find_remainder([1, 2, 3], 3, -10)
