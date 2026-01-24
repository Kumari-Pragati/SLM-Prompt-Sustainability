import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_num([]), 0.0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(sum_num([10]), 10.0)

    def test_edge_case_zero_length_list(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([])

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([0])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_num([-1, -2, -3, -4, -5]), -3.0)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(sum_num([1, -2, 3, -4, 5]), 1.0)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sum_num([1, 2, 'a', 4, 5])
