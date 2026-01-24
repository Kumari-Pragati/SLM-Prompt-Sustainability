import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_add_string_typical(self):
        self.assertEqual(add_string([1, 2, 3], "Hello"), ["Hello1", "Hello2", "Hello3"])

    def test_add_string_edge_case_empty_list(self):
        self.assertEqual(add_string([], "Hello"), [])

    def test_add_string_edge_case_empty_string(self):
        self.assertEqual(add_string([1, 2, 3], ""), [])

    def test_add_string_edge_case_single_element_list(self):
        self.assertEqual(add_string([1], "Hello"), ["Hello1"])

    def test_add_string_edge_case_single_element_string(self):
        self.assertEqual(add_string([1, 2, 3], "Hello"), ["Hello1", "Hello2", "Hello3"])

    def test_add_string_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            add_string("not a list", "Hello")

    def test_add_string_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            add_string([1, 2, 3], 123)
