import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ["1", "2", "3"])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_string([], "{}"), [])

    def test_edge_case_empty_string(self):
        self.assertEqual(add_string([1, 2, 3], ""), ["1", "2", "3"])

    def test_edge_case_string_with_no_format(self):
        self.assertEqual(add_string([1, 2, 3], "Hello"), ["Hello", "Hello", "Hello"])

    def test_edge_case_list_with_non_integer(self):
        self.assertEqual(add_string(["a", 2, 3], "{}"), ["a", str(2), str(3)])

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(add_string([-1, 2, -3], "{}"), ["-1", "2", "-3"])
