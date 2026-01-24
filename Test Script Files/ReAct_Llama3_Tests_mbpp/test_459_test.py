import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_uppercase(""), "")

    def test_all_lowercase(self):
        self.assertEqual(remove_uppercase("hello"), "hello")

    def test_all_uppercase(self):
        self.assertEqual(remove_uppercase("HELLO"), "")

    def test_mixed_case(self):
        self.assertEqual(remove_uppercase("HeLlO"), "llo")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            remove_uppercase(None)
