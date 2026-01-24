import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_odd([1]), 1)

    def test_edge_case_all_even(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_edge_case_all_odd(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_edge_case_mixed(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_edge_case_zero(self):
        self.assertEqual(count_odd([0, 1, 2, 3, 4, 5]), 3)
