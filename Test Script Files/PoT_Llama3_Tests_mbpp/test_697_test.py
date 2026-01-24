import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_even([1]), 0)

    def test_edge_case_single_even_element(self):
        self.assertEqual(count_even([2]), 1)

    def test_edge_case_single_odd_element(self):
        self.assertEqual(count_even([3]), 0)

    def test_edge_case_multiple_even_elements(self):
        self.assertEqual(count_even([2, 4, 6]), 3)

    def test_edge_case_multiple_odd_elements(self):
        self.assertEqual(count_even([1, 3, 5]), 0)

    def test_edge_case_mixed_elements(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5]), 2)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, -6]), 3)

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, 2, 4, 6]), 3)
