import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_length("100100", 10), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_length("0", 1), 0)

    def test_edge_case_one(self):
        self.assertEqual(find_length("1", 1), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(find_length("", 5), 0)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            find_length(None, 5)

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_length("abc", "abc")

    def test_edge_case_invalid_input_length(self):
        with self.assertRaises(TypeError):
            find_length("100100", -1)
