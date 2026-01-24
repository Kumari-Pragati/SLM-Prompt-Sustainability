import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_length(["apple", "banana", "cherry"]), (7, "cherry"))

    def test_edge_case(self):
        self.assertEqual(max_length(["apple", "banana"]), (6, "banana"))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(["apple"]), (5, "apple"))

    def test_max_length_equal(self):
        self.assertEqual(max_length(["apple", "banana", "cherry", "date"]), (7, "cherry"))

    def test_max_length_not_equal(self):
        self.assertEqual(max_length(["apple", "banana", "cherry", "date", "elderberry"]), (12, "elderberry"))

    def test_max_list_is_not_max_length(self):
        self.assertEqual(max_length(["apple", "banana", "cherry", "date", "elderberry", "fig"]), (12, "elderberry"))

    def test_max_list_is_max_length(self):
        self.assertEqual(max_length(["apple", "banana", "cherry", "date", "elderberry", "fig", "elderberry"]), (12, "elderberry"))
