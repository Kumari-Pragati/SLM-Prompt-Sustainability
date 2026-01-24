import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 3)

    def test_edge_case_zero_length_array(self):
        self.assertEqual(find_remainder([], 3, 5), 1)

    def test_edge_case_one_element_array(self):
        self.assertEqual(find_remainder([1], 3, 5), 1)

    def test_edge_case_one_element_array_n_equals_two(self):
        self.assertEqual(find_remainder([1], 1, 2), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_remainder([-1, 2, -3], 3, 5), 4)

    def test_edge_case_empty_list_and_n_equals_one(self):
        self.assertEqual(find_remainder([], 1, 1), 0)

    def test_error_case_negative_lens(self):
        with self.assertRaises(IndexError):
            find_remainder([1, 2, 3], -1, 5)
