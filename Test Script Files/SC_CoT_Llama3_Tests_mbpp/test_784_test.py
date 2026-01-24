import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_even_odd([2]), -1)

    def test_edge_case_list_with_no_evens(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_edge_case_list_with_no_odds(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), -1)

    def test_edge_case_list_with_one_even(self):
        self.assertEqual(mul_even_odd([2]), 0)

    def test_edge_case_list_with_one_odd(self):
        self.assertEqual(mul_even_odd([1]), -1)

    def test_edge_case_list_with_multiple_evens(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), 0)

    def test_edge_case_list_with_multiple_odds(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_edge_case_list_with_evens_and_odds(self):
        self.assertEqual(mul_even_odd([2, 3, 4]), 12)
