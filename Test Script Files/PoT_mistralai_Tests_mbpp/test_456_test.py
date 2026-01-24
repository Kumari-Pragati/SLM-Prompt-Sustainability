import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_edge_case_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_edge_case_single_item(self):
        self.assertEqual(reverse_string_list(["abc"]), ["cba"])

    def test_boundary_case_single_char(self):
        self.assertEqual(reverse_string_list(["A"]), ["A"])

    def test_boundary_case_multi_char(self):
        self.assertEqual(reverse_string_list(["AB"]), ["BA"])

    def test_corner_case_empty_string(self):
        self.assertEqual(reverse_string_list([""]), [""])
