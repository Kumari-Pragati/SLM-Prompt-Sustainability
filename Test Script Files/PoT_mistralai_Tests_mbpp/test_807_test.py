import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([5, 4, 3, 2, 1]), 5)
        self.assertEqual(first_odd([-1, 1, 3, 5]), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_edge_case_single_even_number(self):
        self.assertEqual(first_odd([2]), -1)

    def test_edge_case_single_odd_number(self):
        self.assertEqual(first_odd([1]), 1)

    def test_corner_case_all_even(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)
