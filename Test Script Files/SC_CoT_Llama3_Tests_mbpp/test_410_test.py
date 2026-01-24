import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_val([10]), 10)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(min_val([-10, -5, -3, -1]), -10)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(min_val([-10, -5, 1, 2, 3]), -10)

    def test_edge_case_list_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            min_val([1, 2, 'a', 4, 5])

    def test_edge_case_list_with_non_integer_values_and_empty_string(self):
        with self.assertRaises(TypeError):
            min_val([1, 2, 'a', '', 5])
