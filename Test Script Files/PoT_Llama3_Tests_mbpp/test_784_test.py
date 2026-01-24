import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_even_odd([2]), -1)

    def test_edge_case_list_with_no_even(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)

    def test_edge_case_list_with_no_odd(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), -1)

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(mul_even_odd([2]), 2)

    def test_edge_case_list_with_two_elements(self):
        self.assertEqual(mul_even_odd([2, 3]), 6)

    def test_edge_case_list_with_multiple_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6, 8]), 32)

    def test_edge_case_list_with_multiple_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5, 7]), -1)
