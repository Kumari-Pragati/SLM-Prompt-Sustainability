import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_typical_case(self):
        s = "apple apple banana"
        a = 2
        expected = [('apple', 2), ('banana', 1)]
        self.assertEqual(most_common_elem(s, a), expected)

    def test_edge_case_a_zero(self):
        s = "apple apple banana"
        a = 0
        with self.assertRaises(ValueError):
            most_common_elem(s, a)

    def test_edge_case_s_empty(self):
        s = ""
        a = 1
        expected = []
        self.assertEqual(most_common_elem(s, a), expected)

    def test_edge_case_a_greater_than_s_length(self):
        s = "apple apple banana"
        a = 5
        expected = [('apple', 2), ('banana', 1)]
        self.assertEqual(most_common_elem(s, a), expected)

    def test_edge_case_s_single_element(self):
        s = "apple"
        a = 1
        expected = [('apple', 1)]
        self.assertEqual(most_common_elem(s, a), expected)

    def test_edge_case_s_all_unique(self):
        s = "apple banana orange"
        a = 3
        expected = [('apple', 1), ('banana', 1), ('orange', 1)]
        self.assertEqual(most_common_elem(s, a), expected)
