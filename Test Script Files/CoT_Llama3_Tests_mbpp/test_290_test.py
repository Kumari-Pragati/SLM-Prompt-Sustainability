import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_length(["apple", "banana", "cherry"]), (7, "apple"))

    def test_edge_case(self):
        self.assertEqual(max_length(["apple", "banana", "cherry", "date"]), (5, "date"))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(["apple"]), (5, "apple"))

    def test_list_with_duplicates(self):
        self.assertEqual(max_length(["apple", "banana", "apple", "cherry"]), (7, "apple"))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length(["apple", "", "banana", "cherry"]), (7, "apple"))

    def test_list_with_mixed_types(self):
        self.assertEqual(max_length(["apple", 1, "banana", "cherry"]), (7, "apple"))
