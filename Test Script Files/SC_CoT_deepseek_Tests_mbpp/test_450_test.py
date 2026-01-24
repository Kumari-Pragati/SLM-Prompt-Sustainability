import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_string(["abc", "def", "ghi"], 3), ["abc", "def", "ghi"])

    def test_empty_string(self):
        self.assertEqual(extract_string([""], 0), [""])

    def test_edge_case_with_empty_list(self):
        self.assertEqual(extract_string([], 3), [])

    def test_edge_case_with_zero_length(self):
        self.assertEqual(extract_string(["abc", "def", "ghi"], 0), [])

    def test_special_case_with_mixed_lengths(self):
        self.assertEqual(extract_string(["abc", "de", "fghi"], 3), ["abc", "fghi"])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_string(123, 3)

    def test_invalid_length_input(self):
        with self.assertRaises(TypeError):
            extract_string(["abc", "def", "ghi"], "3")
