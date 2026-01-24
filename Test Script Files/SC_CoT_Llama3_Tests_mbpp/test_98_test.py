import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(multiply_num([1, 2, 3]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiply_num([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_edge_case_single_element_list_zero(self):
        self.assertEqual(multiply_num([0]), 0)

    def test_edge_case_single_element_list_negative(self):
        self.assertEqual(multiply_num([-1]), -1)

    def test_edge_case_single_element_list_positive(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_edge_case_single_element_list_negative_and_positive(self):
        self.assertEqual(multiply_num([-1, 1]), 0)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 3)

    def test_edge_case_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([1, 2, 3, 4, 5, 0])

    def test_edge_case_division_by_zero_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([1, 2, 3, 4, 5, 0, 0])
