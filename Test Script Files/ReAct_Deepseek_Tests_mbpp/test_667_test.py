import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_edge_case_no_vowels(self):
        self.assertEqual(Check_Vow("bcdfghjklmnpqrstvwxyz", "aeiou"), 0)

    def test_edge_case_all_vowels(self):
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)

    def test_explicitly_handled_error_case(self):
        with self.assertRaises(TypeError):
            Check_Vow(12345, "aeiou")
