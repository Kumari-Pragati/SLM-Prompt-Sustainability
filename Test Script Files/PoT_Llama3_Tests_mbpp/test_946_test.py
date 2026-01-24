import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(most_common_elem('apple apple apple banana', 2), [('apple', 3), ('banana', 1)])

    def test_edge_case_a_zero(self):
        with self.assertRaises(ValueError):
            most_common_elem('apple apple apple banana', 0)

    def test_edge_case_s_empty(self):
        self.assertEqual(most_common_elem('', 1), [])

    def test_edge_case_a_one(self):
        self.assertEqual(most_common_elem('apple apple apple banana', 1), [('apple', 3)])

    def test_edge_case_s_single_element(self):
        self.assertEqual(most_common_elem('apple', 1), [('apple', 1)])

    def test_edge_case_s_multiple_elements(self):
        self.assertEqual(most_common_elem('apple banana apple', 2), [('apple', 2), ('banana', 1)])

    def test_edge_case_s_duplicates(self):
        self.assertEqual(most_common_elem('apple apple apple', 2), [('apple', 3)])
