import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)

    def test_edge_case_zero(self):
        self.assertEqual(find_remainder([1, 2, 3], 0, 4), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_remainder([1], 1, 4), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_remainder([], 0, 4), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 0), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 1), 1)

    def test_edge_case_larger_array(self):
        self.assertEqual(find_remainder([1, 2, 3, 4, 5, 6], 6, 4), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_remainder([-1, -2, -3], 3, 4), 1)

    def test_edge_case_large_numbers(self):
        self.assertEqual(find_remainder([1000000, 2000000, 3000000], 3, 4), 1)
