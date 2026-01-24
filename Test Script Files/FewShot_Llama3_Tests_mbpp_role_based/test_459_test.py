import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_uppercase("Hello World"), "ello world")

    def test_empty_string(self):
        self.assertEqual(remove_uppercase(""), "")

    def test_single_character_string(self):
        self.assertEqual(remove_uppercase("A"), "")

    def test_all_uppercase_string(self):
        self.assertEqual(remove_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "")

    def test_mixed_case_string(self):
        self.assertEqual(remove_uppercase("HeLlO wOrLd"), "ello world")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)
