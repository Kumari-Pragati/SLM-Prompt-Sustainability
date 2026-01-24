import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_even_odd([1, 2, 3, 4]), 8)

    def test_edge_case_no_even(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_edge_case_no_odd(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), -1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(mul_even_odd([]), -1)

    def test_corner_case_single_element(self):
        self.assertEqual(mul_even_odd([2]), -1)

    def test_corner_case_all_same_elements(self):
        self.assertEqual(mul_even_odd([2, 2, 2]), 4)

    def test_corner_case_all_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), 48)

    def test_corner_case_all_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), 15)
