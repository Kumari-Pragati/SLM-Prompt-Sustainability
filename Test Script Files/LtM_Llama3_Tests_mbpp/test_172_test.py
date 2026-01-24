import unittest
from mbpp_172_code import count_occurance

class TestCountOcurance(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_occurance(""), 0)

    def test_no_match(self):
        self.assertEqual(count_occurance("hello"), 0)

    def test_single_match(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_multiple_matches(self):
        self.assertEqual(count_occurance("stdstd"), 2)

    def test_edge_case(self):
        self.assertEqual(count_occurance("stdstdstd"), 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_occurance(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            count_occurance([1, 2, 3])
