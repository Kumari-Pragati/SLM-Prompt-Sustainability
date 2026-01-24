import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_val([1]), 1)

    def test_edge_case_single_element_list_non_integer(self):
        self.assertIsNone(max_val(['a']))

    def test_edge_case_single_element_list_non_integer_and_int(self):
        self.assertEqual(max_val([1, 'a']), 1)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case_multiple_elements_list_non_integer(self):
        self.assertEqual(max_val([1, 2, 'a', 4, 5]), 5)

    def test_edge_case_multiple_elements_list_non_integer_and_int(self):
        self.assertEqual(max_val([1, 2, 'a', 4, 5, 6]), 6)

    def test_edge_case_multiple_elements_list_non_integer_and_int_and_float(self):
        self.assertEqual(max_val([1, 2, 'a', 4, 5, 6.5]), 6.5)

    def test_edge_case_multiple_elements_list_non_integer_and_int_and_float_and_string(self):
        self.assertEqual(max_val([1, 2, 'a', 4, 5, 6.5, 'c']), 6.5)
