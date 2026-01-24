import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(filter_oddnumbers([10]), [])

    def test_edge_case_single_odd_number(self):
        self.assertEqual(filter_oddnumbers([5]), [5])

    def test_edge_case_multiple_odd_numbers(self):
        self.assertEqual(filter_oddnumbers([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_edge_case_multiple_even_numbers(self):
        self.assertEqual(filter_oddnumbers([2, 4, 6, 8, 10]), [])

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(filter_oddnumbers([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_edge_case_zero(self):
        self.assertEqual(filter_oddnumbers([0, 1, 2, 3, 4, 5]), [])

    def test_edge_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            filter_oddnumbers([1, 2, 3, 'a', 4, 5])
