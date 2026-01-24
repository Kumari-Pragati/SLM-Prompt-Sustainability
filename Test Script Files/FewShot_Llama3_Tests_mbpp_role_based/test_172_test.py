import unittest
from mbpp_172_code import count_occurance

class TestCountOcurance(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_occurance(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count_occurance("t"), 0)

    def test_edge_case_no_match(self):
        self.assertEqual(count_occurance("hello"), 0)

    def test_edge_case_multiple_matches(self):
        self.assertEqual(count_occurance("stdstdstd"), 3)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            count_occurance(123)
