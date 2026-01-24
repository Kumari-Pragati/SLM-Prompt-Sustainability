import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_val([1]), 1)

    def test_edge_case_all_non_integers(self):
        self.assertIsNone(max_val(['a', 'b', 'c']))

    def test_edge_case_mixed_types(self):
        self.assertEqual(max_val([1, 'a', 3, 'b', 5]), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -5)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_case_zero(self):
        self.assertEqual(max_val([0, 1, 2, 3, 4]), 4)

    def test_edge_case_negative_and_positive_numbers(self):
        self.assertEqual(max_val([-1, 0, 1, 2, 3]), 3)
