import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_edge_case_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            div_even_odd([])

    def test_edge_case_single_element_list(self):
        self.assertEqual(div_even_odd([2]), -1)

    def test_edge_case_single_even_element_list(self):
        self.assertEqual(div_even_odd([2]), -1)

    def test_edge_case_single_odd_element_list(self):
        self.assertEqual(div_even_odd([3]), -1)

    def test_edge_case_multiple_even_elements_list(self):
        self.assertEqual(div_even_odd([2, 4, 6]), 2/4)

    def test_edge_case_multiple_odd_elements_list(self):
        self.assertEqual(div_even_odd([3, 5, 7]), 3/5)

    def test_edge_case_list_with_mixed_elements(self):
        self.assertEqual(div_even_odd([2, 3, 4, 5]), 2/3)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(div_even_odd([2, 2, 3, 3]), 2/3)

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(div_even_odd([-2, 3, 4, 5]), -2/3)

    def test_edge_case_list_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_even_odd([0, 3])

    def test_edge_case_list_with_negative_and_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_even_odd([-2, 0, 3])
