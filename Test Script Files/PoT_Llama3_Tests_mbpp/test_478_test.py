import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HW")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_edge_case_all_lowercase(self):
        self.assertEqual(remove_lowercase("abcdefghijklmnopqrstuvwxyz"), "")

    def test_edge_case_all_uppercase(self):
        self.assertEqual(remove_lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_lowercase("HelloWorld123"), "HW123")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)

    def test_edge_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            remove_lowercase(None)

    def test_edge_case_non_string_input3(self):
        with self.assertRaises(TypeError):
            remove_lowercase([1, 2, 3])
