import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_val([1]), 1)

    def test_edge_case_list_with_non_int(self):
        self.assertEqual(max_val([1, 2, 'a', 4]), 4)

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, 3, 4]), 4)

    def test_edge_case_list_with_positive_numbers(self):
        self.assertEqual(max_val([1, 2, 3, 4]), 4)

    def test_edge_case_list_with_mixed_numbers(self):
        self.assertEqual(max_val([-1, 0, 1, 2]), 2)
