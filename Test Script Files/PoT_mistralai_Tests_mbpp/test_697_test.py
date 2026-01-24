import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_even([2, 4, 6, 8]), 4)

    def test_edge_case_min(self):
        self.assertEqual(count_even([0]), 1)

    def test_edge_case_max(self):
        self.assertEqual(count_even([1000000000]), 0)

    def test_boundary_case_min(self):
        self.assertEqual(count_even([-2]), 1)

    def test_boundary_case_max(self):
        self.assertEqual(count_even([2000000000]), 0)

    def test_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_single_odd_number(self):
        self.assertEqual(count_even([1]), 0)

    def test_single_even_number(self):
        self.assertEqual(count_even([2]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(count_even([1, 3, 5, 2, 4, 6]), 4)
